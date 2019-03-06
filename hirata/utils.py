import hirata.conf as conf
import logging
import re
import sys

logger = logging.getLogger("main")
logging.basicConfig(level=logging.DEBUG)


def translate_indices(atom):
    """Translate h1 -> some indices
    which are defined in the configuration file.
    """
    for index_trans in [conf.PARTICLE_INDICES, conf.HOLE_INDICES]:
        for index in index_trans.keys():
            if index_trans[index] is not None:
                atom = re.sub(index, index_trans[index], atom)
    return atom


def transform_tensor_indices(atom):
    """For example (a b i j) -> ["abij"]
    """
    atom = re.sub(" ", "", atom)
    atom = re.sub("\(", "[\"", atom)
    atom = re.sub("\)", "\"]", atom)
    return atom








def permute_indices(index, start_indices, permuted_indices):
    try:
        from string import maketrans
    except:
        maketrans = str.maketrans
    assert(len(start_indices) == len(permuted_indices))
    new_index = index
    changed=[]
    trans_table = maketrans(start_indices, permuted_indices)
    new_index = index.translate(trans_table)
    return new_index


def permute_cc4s_index(atom, start_indices, permuted_indices):
    # print(atom)
    ii = re.match(r".*\"(.*)\".*", atom)
    index = ii.group(1)
    istart = ii.start()
    iend = ii.end()
    new_index = permute_indices(index, start_indices, permuted_indices)
    # print("index         : %s (%s - %s)" % (index, istart, iend))
    # print("new_index     : %s " % (new_index))
    new_line = atom.replace(index, new_index)
    return new_line


def cc4s_to_cpp(cc4s_line):
    """Convert a cc4s line class into cpp code
    """
    logger = logging.getLogger("cc4s_to_cpp")
    result = []
    result_line = ""
    for prefactor in cc4s_line.get_prefactors():
        if not re.match(r".*P.*", prefactor):
            # Identity
            start_indices = "a"
            permuted_indices = "a"
        else:
            start_indices = re.match(r".*\((.*)=>.*", prefactor)\
                .group(1).replace(" ", "")
            permuted_indices = re.match(r".*=>(.*)\).*", prefactor)\
                .group(1).replace(" ", "")
        prefactor_val = re.sub(r"\*\sP.*", "", prefactor)
        logger.debug("Start indices = %s", start_indices)
        logger.debug("Permuted indices = %s", permuted_indices)
        logger.debug("Prefactor value = %s", prefactor_val)
        result_line = "( %s )" % prefactor_val
        for postfactor in cc4s_line.get_postfactors():
            result_line += " * %s" % permute_cc4s_index(postfactor, start_indices, permuted_indices)
        result.append(result_line+";")
    return result



def get_tensor_name_with_indices(name, hp_partition, indices):
    """For example it should do
    T , abij, klbc -> Tabij["bclk"]
    T , abcj, klbc -> error because klbc is not pphh or any combination
    :returns: String containing the tensor expression
    """
    particles = conf.PARTICLE_INDICES.values()
    ordered_indices = ""
    holes = conf.HOLE_INDICES.values()
    hole_indices = [i for i in indices if i in holes]
    particle_indices = [i for i in indices if i in particles]
    # sort
    hole_indices.sort()
    particle_indices.sort()
    if not len([i for i in hp_partition if i in holes]) == len(hole_indices):
        logger.error("%s must have as many holes as %s" % (hp_partition, indices))
        sys.exit(1)
    if not len(hp_partition) == len(indices):
        logger.error("%s must have as many indices as %s" % (hp_partition, indices))
        sys.exit(1)
    for k in hp_partition:
        if k in holes:
            ordered_indices += hole_indices[0]
            hole_indices.pop(0)
        else:
            ordered_indices += particle_indices[0]
            particle_indices.pop(0)
    tensor_name = "{tensor}{partition}[\"{indices}\"]".format(
        tensor=name,
        partition=hp_partition,
        indices=ordered_indices
    )
    return tensor_name


def process_file(args):
    result_lines = []
    logger.info("Processing %s ", args.file)
    indices = None
    fd = open(args.file)
    for line in fd:
        print("")
        h_line = HirataLine(line)
        cc4s_line = hirata_to_cc4s(h_line)
        lines = cc4s_to_cpp(cc4s_line)
        removed_cause_fock = False
        if args.fock and re.match(r".*(Fai|Fia).*", ",".join(lines)):
            logger.debug("Killing fock contributions")
            removed_cause_fock = True
            lines = ["// <FOCK> " + li for li in lines]
        result_lines.append("// orig  : %s" % line.replace("\n", ""))
        result_lines.append("// conv  : %s" % cc4s_line.get_printable_atoms())
        result_lines.append("// free  : %s" % cc4s_line.get_free_indices())
        result_lines.append("// summed: %s" % cc4s_line.get_summation_indices())
        if args.contract_with:
            if args.with_indices:
                indices = args.with_indices
            tensor_name = get_tensor_name_with_indices(
                args.contract_with,
                args.with_indices,
                cc4s_line.get_free_indices().replace(" ", "")
            )
            logger.debug("Contracting with tensor %s" % tensor_name)
            lines = [
                re.sub(r"\)\s*\*\s*", ") * %s * " % tensor_name, li)
                for li in lines
            ]
        if args.python_tuples_out and not removed_cause_fock:
            with open(args.python_tuples_out, 'a+') as fd:
                for line in lines:
                    fd.write(
                    str(
                        line.replace(' ', '').replace(';', '').split('*')[1:]
                    )
                    )
                    fd.write('\n')
        if args.prepend:
            logger.debug("Prepending %s" % args.prepend)
            lines = [args.prepend + li for li in lines]
        if args.with_intermediates and not removed_cause_fock:
            if args.with_indices:
                indices = args.with_indices
            tensor_name = args.with_intermediates
            free_indices = cc4s_line.get_free_indices().replace(" ", "")
            tensor = get_tensor_name_with_indices(
                tensor_name,
                indices,
                free_indices
            )
            logger.debug("Intermediate %s" % tensor)
            lines = [
                "%s = %s" % (tensor, li)
                for li in lines
            ]
        result_lines += lines
        result_lines.append("")
    if args.no_comments:
        logger.debug("Getting rid of comments")
        result_lines = [li for li in result_lines if not re.match(r"^//.*$", li)]
    return result_lines


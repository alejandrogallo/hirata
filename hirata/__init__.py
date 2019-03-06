#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import logging
import argparse
try:
    import conf
except Exception as e:
    print("You need a configuration to run this!!")
    sys.exit(1)


logger = logging.getLogger("main")
logging.basicConfig(level=logging.DEBUG)

conf_variables = [
    "conf.PARTICLE_INDICES",
    "conf.HOLE_INDICES",
    "conf.TENSOR_NAME_TRANSLATON",
    "conf.TENSOR_INDICES_TRANSLATION",
]
logger.debug("Checking if all configuration variables are defined")
for conf_var in conf_variables:
    try:
        eval(conf_var)
    except Exception as e:
        print("I could not find the variable %s in the configuration" % conf_var)
        sys.exit(1)

class HirataLine(object):

    """Implements a complete representation of every line in the Hirata
    equations"""

    def __init__(self, line):
        self.atoms = None
        self.raw_line = line.replace("\n", "")
        self.prefactors = None
        self.postfactors = None
        self.summation_indices = None
        self.free_indices = None
        self.logger = logging.getLogger("HirataLine")

        # If we should translate also the projector operators into some other
        # implementation that we might have at hand
        self.with_projector = False
        self.parse()

    def parse(self):
        self.get_free_indices()
        self.get_summation_indices()
        self.get_postfactors()
        self.get_prefactors()

    def set_free_indices(self, indices): self.free_indices = indices
    def get_free_indices(self):
        if self.free_indices is not None: return self.free_indices
        postfactors = self.get_postfactors()
        summation_indices = self.get_summation_indices() or ""
        free_indices = ""
        for factor in postfactors:
            indices = re.match(r".*\((.*)\).*", factor).group(1).split()
            for index in indices:
                if index not in summation_indices and index not in free_indices:
                    free_indices += " " + index
        self.free_indices = free_indices
        self.logger.debug("Free indices = %s", self.free_indices)
        return self.free_indices

    def set_summation_indices(self, indices): self.summation_indices = indices
    def get_summation_indices(self):
        if self.summation_indices is not None: return self.summation_indices
        for atom in self.get_atoms()[1:]:
            m = re.match(r"\s*Sum\s*\((.*)\)\s*", atom)
            if m:
                self.summation_indices = m.group(1)
                self.logger.debug("Summation indices = %s", self.summation_indices)
                return self.summation_indices

    def set_postfactors(self, postfactors): self.postfactors = postfactors
    def get_postfactors(self):
        """If postfactors were not parsed before, parse postfactors from raw_line.
        Thankfully Hirata atomic structures are separated always by asterisks.
        :returns: Atoms
        """
        if self.postfactors is not None: return self.postfactors
        try:
            assert self.raw_line[0] == "["
        except Exception as e:
            self.logger.error("The first char of every line should be a [")
            sys.exit(1)
        # Split the end of the prefactor parenthesis
        self.postfactors = re.split(r"\]\s*\*\s*", self.raw_line)
        # Get rid of the other parenthesis
        self.postfactors[0] = self.postfactors[0].replace("[", "")
        # Get rid of empty strings
        self.postfactors[0] = [s for s in re.split(r"\s*([+-][^+-]+)\s*", self.postfactors[0]) if len(s)]
        self.set_prefactors(self.postfactors[0])
        self.logger.debug("prefactors = %s", self.prefactors)
        # Split the rest of the string in terms of products with * operator
        post_factor = self.postfactors.pop(1)
        self.postfactors = re.split(r"\s*\*\s*", post_factor)
        self.logger.debug("postfactors = %s", self.postfactors)
        return self.postfactors


    def set_atoms(self, atoms): self.atoms = atoms
    def get_atoms(self):
        """If atoms were not parsed before, parse atoms from raw_line.
        Thankfully Hirata atomic structures are separated always by asterisks.
        :returns: Atoms
        """
        return [self.get_prefactors()] + self.get_postfactors()

    def get_printable_atoms(self):
        """Get atoms in the form that should be printed according to hirata
        """
        return "[ " + "".join(self.get_prefactors()) + " ] * " + " * ".join(self.get_postfactors())

    def set_prefactors(self, prefactors): self.prefactors = prefactors
    def get_prefactors(self):
        # get first postfactors
        self.get_postfactors()
        if self.prefactors is not None:
            return self.prefactors


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


def get_hp_combination(atom):
    """Get if tensor is of type hhhh, hhpp, hh, hp etc...
    """
    return "".join(re.findall(r"([hp])[0-9]+", atom))


def get_converted_hp_combination(atom):
    """Get if tensor is of type hp, hhpp, hh, hp etc...
    """
    hp = get_hp_combination(atom)
    for pppp in conf.TENSOR_INDICES_TRANSLATION.keys():
        abij = conf.TENSOR_INDICES_TRANSLATION[pppp]
        if hp[0:len(hp)] == pppp[0:len(hp)]:
            return abij[0: len(hp)]
    return hp


def translate_tensor_names(atom):
    """Translate t( h p ) -> Tia
        which are defined in the configuration file.
    """
    for name in conf.TENSOR_NAME_TRANSLATON:
        converted_index = get_converted_hp_combination(atom)
        tensor_name = conf.TENSOR_NAME_TRANSLATON[name]
        atom = re.sub(
            name,
            tensor_name.format(hpindices=converted_index),
            atom
        )
    return atom


def permute_indices(index, start_indices, permuted_indices):
    import string
    assert(len(start_indices) == len(permuted_indices))
    new_index = index
    changed=[]
    trans_table = string.maketrans(start_indices, permuted_indices)
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


def hirata_to_cc4s(hirata_line):
    """Convert a hirata line to cc4s
    """
    import copy
    line = copy.copy(hirata_line)
    logger = logging.getLogger("hirata_to_cc4s")

    # Post factors
    logger.debug("Doing postfactors")
    postfactors = []
    for factor in line.get_postfactors():
        if re.match(r"Sum", factor):
            continue
        factor = translate_tensor_names(factor)
        factor = translate_indices(factor)
        factor = transform_tensor_indices(factor)
        postfactors.append(factor)
    line.set_postfactors(postfactors)
    logger.debug("Postfactors = %s", line.get_postfactors())

    # Pre factors
    logger.debug("Doing prefactors")
    prefactors = []
    for factor in line.get_prefactors():
        factor = translate_indices(factor)
        prefactors.append(factor)
    line.set_prefactors(prefactors)
    logger.debug("Prefactors = %s", line.get_prefactors())

    if line.get_summation_indices() is not None:
        line.set_summation_indices(
            translate_indices(line.get_summation_indices())
        )
        logger.debug("Summation indices= %s", line.get_summation_indices())
    line.set_free_indices(
        translate_indices(line.get_free_indices())
    )
    logger.debug("Free indices= %s", line.get_free_indices())

    logger.debug(" Atoms = %s", line.get_printable_atoms())

    return line


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


if __name__ == "__main__":
    main()


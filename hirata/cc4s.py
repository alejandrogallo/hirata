import re
import copy
from .line import HirataLine
import hirata.conf as conf
from .utils import permute_indices
import logging


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

def transform_tensor_indices(atom):
    """For example (a b i j) -> ["abij"]
    """
    atom = re.sub(" ", "", atom)
    atom = re.sub("\(", "[\"", atom)
    atom = re.sub("\)", "\"]", atom)
    return atom


def translate_indices(atom):
    """Translate h1 -> some indices
    which are defined in the configuration file.
    """
    for index_trans in [conf.PARTICLE_INDICES, conf.HOLE_INDICES]:
        for index in index_trans.keys():
            atom = re.sub(
                r"({index})([ \)])".format(index=index),
                r"{newindex}\2".format(newindex=index_trans[index]),
                atom
            )
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


class Cc4sLine:
    def __init__(self, hirata_line):
        assert(isinstance(hirata_line, HirataLine))
        self.hl = copy.copy(hirata_line)
        self.postfactors = []
        self.prefactors = []
        self.summation_indices = None
        self.free_indices = None
        self.parse()

    def parse(self):
        logger = logging.getLogger("cc4s")

        # Post factors
        logger.debug("Doing postfactors")
        for factor in self.hl.get_postfactors():
            if re.match(r"Sum", factor):
                continue
            factor = translate_tensor_names(factor)
            factor = translate_indices(factor)
            factor = transform_tensor_indices(factor)
            self.postfactors.append(factor)
        logger.debug("Postfactors = %s", self.postfactors)

        # Pre factors
        logger.debug("Doing prefactors")
        for factor in self.hl.get_prefactors():
            factor = translate_indices(factor)
            self.prefactors.append(factor)
        logger.debug("Prefactors = %s", self.prefactors)

        if self.hl.get_summation_indices() is not None:
            self.summation_indices = translate_indices(
                self.hl.get_summation_indices()
            )
            logger.debug("Summation indices= %s", self.summation_indices)
        self.free_indices = translate_indices(self.hl.get_free_indices() + " ")
        logger.debug("Free indices= %s", self.free_indices)

        logger.debug(" Atoms = %s", self)

    def __repr__(self):
        return "[ {prefactors} ] * ( {postfactors} )".format(
            prefactors=" ".join(self.prefactors),
            postfactors=" *prefactors ".join(self.postfactors),
        )


    def to_cpp(self):
        """Convert a cc4s line class into cpp code
        """
        logger = logging.getLogger("cc4s_to_cpp")
        result = []
        result_line = ""
        for prefactor in self.prefactors:
            if not re.match(r".*P.*", prefactor):
                # Identity
                start_indices = "a"
                permuted_indices = "a"
            else:
                start_indices = (
                    re.match(r".*\((.*)=>.*", prefactor).group(1)
                    .replace(" ", "")
                )
                permuted_indices = (
                    re.match(r".*=>(.*)\).*", prefactor).group(1)
                    .replace(" ", "")
                )
            prefactor_val = re.sub(r"\*\sP.*", "", prefactor)
            logger.debug("Start indices = %s", start_indices)
            logger.debug("Permuted indices = %s", permuted_indices)
            logger.debug("Prefactor value = %s", prefactor_val)
            result_line = "( %s )" % prefactor_val
            for postfactor in self.postfactors:
                result_line += " * %s" % permute_cc4s_index(
                    postfactor,
                    start_indices,
                    permuted_indices
                )
            result.append(result_line+";")
        return result

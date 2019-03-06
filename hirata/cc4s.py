import re
import copy
from .line import HirataLine
import hirata.conf as conf
from .utils import (
    translate_indices,
    transform_tensor_indices
)
import logging


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
        self.free_indices = translate_indices(self.hl.get_free_indices())
        logger.debug("Free indices= %s", self.free_indices)

        logger.debug(" Atoms = %s", self)

    def __repr__(self):
        return "[ {prefactors} ] * ( {postfactors} )".format(
            " ".join(self.prefactors),
            " *prefactors ".join(self.postfactors),
        )

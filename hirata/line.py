import logging
import re
import sys

logger = logging.getLogger("main")
logging.basicConfig(level=logging.DEBUG)

class HirataLine(object):

    """Implements a complete representation of every line in the Hirata
    equations"""

    def __init__(self, line):
        assert(isinstance(line, str))

        self.atoms = None
        self.raw_line = line.replace("\n", "")
        self.prefactors = None
        self.postfactors = None
        self.summation_indices = None
        self.free_indices = None
        self.logger = logging.getLogger("HirataLine")

        self.parse()

    def parse(self):
        self.get_free_indices()
        self.get_summation_indices()
        self.get_postfactors()
        self.get_prefactors()

    def set_free_indices(self, indices):
        self.free_indices = indices

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

    def set_summation_indices(self, indices):
        self.summation_indices = indices

    def get_summation_indices(self):
        if self.summation_indices is not None: return self.summation_indices
        for atom in self.get_atoms()[1:]:
            m = re.match(r"\s*Sum\s*\((.*)\)\s*", atom)
            if m:
                self.summation_indices = m.group(1)
                self.logger.debug("Summation indices = %s", self.summation_indices)
                return self.summation_indices

    def set_postfactors(self, postfactors):
        self.postfactors = postfactors

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

    def set_prefactors(self, prefactors):
        self.prefactors = prefactors

    def get_prefactors(self):
        # get first postfactors
        self.get_postfactors()
        if self.prefactors is not None:
            return self.prefactors


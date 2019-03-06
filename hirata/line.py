import logging
import re
import sys

logger = logging.getLogger("main")
logging.basicConfig(level=logging.DEBUG)

class HirataLine(object):

    """Implements a complete representation of every line in the Hirata
    equations

    Example

    [ + 0.5 ] * Sum ( h2 h4 p1 p3 ) * t ( p1 h2 ) * t ( p3 h4 ) * v ( h2 h4 p1 p3 )

    Prefactors = ['+ 0.5']
    Postfactors = [
        'Sum ( h2 h4 p1 p3 ) ',
        ' t ( p1 h2 ) ',
        ' t ( p3 h4 ) ',
        ' v ( h2 h4 p1 p3 )'
    ]

    """

    def __init__(self, line):
        assert(isinstance(line, str))

        self.raw_line = line.replace("\n", "")
        self.prefactors = None
        self.postfactors = None
        self.summation_indices = None
        self.free_indices = None
        self.logger = logging.getLogger("HirataLine")

        self.parse()

    def parse(self):
        # prefactors and postfactors
        self.get_atoms()
        # here also summation indices are set
        self.get_free_indices()

    def get_free_indices(self):
        if self.free_indices is not None:
            return self.free_indices
        summation_indices = self.get_summation_indices() or ""
        summation_set = set(summation_indices.split())
        regex = re.compile(r".*\((.*)\).*")
        postfactor_set = set(sum(
            (regex.match(f).group(1).split() for f in self.get_postfactors()),
            []
        ))
        self.free_indices = " ".join(list(postfactor_set - summation_set))
        self.logger.debug("Free indices = %s", self.free_indices)
        return self.free_indices

    def get_summation_indices(self):
        if self.summation_indices is not None: return self.summation_indices
        for atom in self.get_atoms()[1:]:
            m = re.match(r"\s*Sum\s*\((.*)\)\s*", atom)
            if m:
                self.summation_indices = m.group(1)
                self.logger.debug("Summation indices = %s", self.summation_indices)
                return self.summation_indices

    def get_postfactors(self):
        """If postfactors were not parsed before, parse postfactors from raw_line.
        Thankfully Hirata atomic structures are separated always by asterisks.
        :returns: Atoms
        """
        if self.postfactors is not None:
            return self.postfactors
        assert self.raw_line[0] == "["
        # Split the end of the prefactor parenthesis
        self.postfactors = re.split(r"\]\s*\*\s*", self.raw_line)
        # Get rid of the other parenthesis
        self.postfactors[0] = self.postfactors[0].replace("[", "")
        # Get rid of empty strings
        self.postfactors[0] = [s for s in re.split(r"\s*([+-][^+-]+)\s*", self.postfactors[0]) if len(s)]
        self.prefactors = self.postfactors[0]
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

    def get_prefactors(self):
        # get first postfactors
        self.get_postfactors()
        return self.prefactors

    def __repr__(self):
        return self.raw_line

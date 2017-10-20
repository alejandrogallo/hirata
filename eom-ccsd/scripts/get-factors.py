#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re

script_dir = os.path.dirname(__file__)
equations_file = os.path.join(
    script_dir, '..', 'factors', 'equations.py'
)
print('Getting factors')
print(equations_file)

class Tensor:
    def __init__(self, string):
        """
        >>> Tensor('Tai*Vijab["jdnh"]') in \
            [Tensor('Vijab*Rai["noei"]'), \
            Tensor('Tai*Tai*Tai["ejcndo"]'),\
            Tensor('Tai*Tai*Vijab["jcoh"]'),\
            Tensor('Tai*Tai*Rai["ejcnhi"]'),\
            Tensor('Tai*Tai*Vijab["jdnh"]'),\
            Tensor('Tai*Tai*Rai["ejdohi"]'),\
            Tensor('Tai*Vijab*Rai["jnoi"]')]
        False
        >>> Tensor('Tai*Tai*Vijab["jdnh"]') in \
            [Tensor('Vijab*Rai["noei"]'), \
            Tensor('Tai*Tai*Tai["ejcndo"]'),\
            Tensor('Tai*Tai*Vijab["jcoh"]'),\
            Tensor('Tai*Tai*Rai["ejcnhi"]'),\
            Tensor('Tai*Tai*Vijab["jdnh"]'),\
            Tensor('Tai*Tai*Rai["ejdohi"]'),\
            Tensor('Tai*Vijab*Rai["jnoi"]')]
        True
        """
        self.string = string
        self.indices = ""
        self.name = ""
        self.parse_indices()
        self.parse_name()
    def __repr__(self): return self.string
    def parse_name(self):
        self.name = re.match(r"(.*)\[(.*)\].*", self.string).group(1)
    def parse_indices(self):
        self.indices = re.match(r".*\[\"(.*)\"\].*", self.string).group(1)
    def __mul__(self, other):
        """
        >>> Tensor('Tabij["abij"]') * Tensor('Vijab["ijab"]')
        Tabij*Vijab[""]
        >>> Tensor('Fij["jk"]') * Tensor('Lia["ka"]')
        Fij*Lia["ja"]
        >>> Tensor('Fij["ji"]') * Tensor('Lia["ka"]')
        Fij*Lia["jika"]
        """
        new_name = self.name + "*" + other.name
        new_indices = "".join(
            [d for d in self.indices if d not in other.indices] +
            [d for d in other.indices if d not in self.indices]
        )
        new = Tensor(new_name+"[\"%s\"]" % new_indices)
        return new
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

def check_compatibility(eqs):
    import itertools
    import operator
    from functools import reduce
    combinations = [
        list(
            itertools.chain.from_iterable(
                itertools.combinations(line, r) for r in range(2, len(line)+1)
            )
        )
        for line in eqs
    ]
    products = [
        [
            reduce(
                operator.mul,
                comb
            ) for comb in line
        ] for line in combinations
    ]
    count = []
    for line in products:
        for prod in line:
            # Get rid of already counted terms
            if prod in [d.get('term') for d in count]: continue
            # print(prod)
            count.append(dict(term=prod, count=0))
            for other_line in products:
                if prod in other_line:
                    count[-1]['count'] += 1
                # for other_prod in other_line:
                    # if other_prod == prod:
                        # print(prod)
    return count

eqs = eval(open(equations_file).read())
eqs_objects = [
    [
        Tensor(element)
        for element in line
    ]
    for line in eqs
]

count = check_compatibility(eqs_objects)

for c in sorted(count, key=lambda x: x[ 'count' ]):
    print("{term!r:<30.30}  {count:<10}".format(**c))




#vim-run: python3 -m doctest % | less

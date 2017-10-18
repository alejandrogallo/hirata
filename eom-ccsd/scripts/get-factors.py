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

eqs = eval(open(equations_file).read())
eqs_objects = [
    [
        Tensor(element)
        for element in line
    ]
    for line in eqs
]

for line in eqs_objects:
    print([d for d in line])

# for line in eqs:
    # print(line)

#vim-run: python3 -m doctest %

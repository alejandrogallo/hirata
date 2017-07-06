#! /usr/bin/env python

import re

terms = [
"L1", "L2",
"R1", "R2"
]

for term in terms:
    cpp_origin = term + ".cpp"
    cpp_out = term + "_out.cpp"
    print("%s >> %s" % (cpp_origin, cpp_out) )
    if term == "L1":
        temp_tensor='X["ja"]'
    if  term == "L1":
        temp_tensor='X["ja"]'
    elif  term == "R1":
        temp_tensor='X["bi"]'
    elif  term == "L2":
        temp_tensor='X["klab"]'
    elif  term == "R2":
        temp_tensor='X["cdij"]'

    fd=open(cpp_origin)
    lines=fd.readlines()
    fd.close()
    fout=cpp_out
    fd=open(fout, "w+")
    for line in lines:
        if re.match(r".*P.*", line):
            continue
        else:
            fd.write('%s += %s;\n' % (temp_tensor, line.replace("\n", "")))

#vim-run: python % && vim L1_out.cpp

#! /usr/bin/env python

def header(msg):    print("\n\033[1;32m"+str(msg)+"\033[0m")
def success(msg):   print(" \033[1;32m==>\033[0m  "+str(msg))
def error(msg):     print(" \033[1;31mX\033[0m  "+str(msg))
def arrow(msg):     print(" \033[1;34m==>\033[0m  "+str(msg))
def warning(msg):   print(" \033[0;93m==>\033[0m  "+str(msg))

import re

terms = [
"R1", "R2"
]

def permute_indices(index, start_indices, permuted_indices):
    assert(not start_indices == permuted_indices)
    assert(len(start_indices) == len(permuted_indices))
    new_index = index
    seen=""
    for i in range(len(start_indices)):
        oi = start_indices[i]
        ni = permuted_indices[i]
        if ni in seen:
            continue
        seen += oi
        new_index = new_index.replace(oi, ni)
    return new_index

def createP(line):
    projectors = re.findall(
        r"[-+]?\s*[0-9]*\.?[0-9]*\s*\*?\s*P\(\s*\"....\",\s*\"....\"\s*\)",
        line
    )
    matches = len(projectors)
    line_without_p = line
    lines = []
    header(line)
    print("# Projectors  : %s"%matches)
    for p in projectors:
        line_without_p = line_without_p.replace(p, "")
    print("Line wout proj: %s"%line_without_p)
    for p in projectors:
        prefactor = re.match(r"[-+]?\s*[0-9]*\.?[0-9]*", p).group(0)
        new_line = re.sub(r"\(.*\)","( %s )" % prefactor, line_without_p, count=1)
        start_indices = re.match(r".*\(\s*\"(....)\"", p).group(1)
        permuted_indices = re.match(r".*,\s*\"(....)\"", p).group(1)
        print("Projector     : %s" % p)
        print("Prefactor     : %s" % prefactor)
        print("Start index   : %s "%start_indices)
        print("Permuted index: %s "%permuted_indices)
        print("new_line      : %s" % new_line)
        indices = re.finditer(r"\"(....)\"", new_line)
        new_indices = []
        for ii in indices:
            index = ii.group(1)
            istart = ii.start()
            iend = ii.end()
            new_index = permute_indices(index, start_indices, permuted_indices)
            print("index         : %s (%s - %s)" % (index, istart, iend))
            print("new_index     : %s " % (new_index))

for term in terms:
    cpp_origin = term + ".cpp"
    cpp_out = term + "_out.cpp"
    print("%s >> %s" % (cpp_origin, cpp_out) )
    if  term == "R1":
        temp_tensor='Lai["ib"]'
    elif  term == "R2":
        temp_tensor='Labij["ijcd"]'

    fd=open(cpp_origin)
    lines=fd.readlines()
    fd.close()
    fout=cpp_out
    fd=open(fout, "w+")
    for line in lines:
        if re.match(r".*P.*", line):
            createP(line.replace("\n", ""))
            # fd.write(line)
        else:
            new_line = re.sub(r"\*", "* " + temp_tensor + " *", line, count=1).replace("\n", "")
            fd.write('energy[""] += %s;\n' % (new_line))

#vim-run: python % 
#vim-run: python % && vim *_out.cpp

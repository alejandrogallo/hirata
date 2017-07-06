#! /usr/bin/env bash

hirata=../hirata.py

set -x

${hirata} -f L1.in -o L1HR1_from_L1.cpp --prepend 'energy[""] = ' --contract-with R --with-indices ai   &&
${hirata} -f L2.in -o L2HR2_from_L2.cpp --prepend 'energy[""] = ' --contract-with R --with-indices abij &&
${hirata} -f R1.in -o L1HR1_from_R1.cpp --prepend 'energy[""] = ' --contract-with L --with-indices ia   &&
${hirata} -f R2.in -o L2HR2_from_R2.cpp --prepend 'energy[""] = ' --contract-with L --with-indices ijab


#vim-run: bash %

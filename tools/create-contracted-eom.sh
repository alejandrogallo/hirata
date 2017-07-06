#! /usr/bin/env bash

SCRIPT_DIR=$(readlink -f $(dirname $0))
hirata=${SCRIPT_DIR}/../hirata.py

if [[ ! -f ${hirata} ]]; then
  echo "You need the ${hirata} script to continue"
  exit 1
fi

if [[ -z $1 ]]; then
  echo "Usage: $(basename $0) <folder-with-L-and-R-equations>"
  exit 1
fi

equations_folder=$1
cd ${equations_folder}

set -x

${hirata} --fock \
  -f L1.in \
  -o L1HR1_from_L1.cpp \
  --prepend 'energy[""] = ' --contract-with R --with-indices ai   &&
${hirata} --fock \
  -f L2.in \
  -o L2HR2_from_L2.cpp \
  --prepend 'energy[""] = ' --contract-with R --with-indices abij &&
${hirata} --fock \
  -f R1.in \
  -o L1HR1_from_R1.cpp \
  --prepend 'energy[""] = ' --contract-with L --with-indices ia   &&
${hirata} --fock \
  -f R2.in \
  -o L2HR2_from_R2.cpp \
  --prepend 'energy[""] = ' --contract-with L --with-indices ijab

cat L1HR1_from_L1.cpp L2HR2_from_L2.cpp > LHR_from_L.cpp
cat L1HR1_from_R1.cpp L2HR2_from_R2.cpp > LHR_from_R.cpp

sed "/\/\//d; /^$/d" LHR_from_L.cpp > LHR_from_L_clean.cpp
sed "/\/\//d; /^$/d" LHR_from_R.cpp > LHR_from_R_clean.cpp

#vim-run: bash %

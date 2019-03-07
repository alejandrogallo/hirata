#! /usr/bin/env bash

SCRIPT_DIR=$(readlink -f $(dirname $0))
hirata=hirata

if [[ -z $1 ]]; then
  echo "Usage: $(basename $0) <folder-with-L-and-R-equations>"
  exit 1
fi

equations_folder=$1
cd ${equations_folder}

folder=contracted

set -x

${hirata} \
  -f L1.in \
  -o ${folder}/L1HR1_from_L1.cpp \
  --prepend 'energy[""] = ' --contract-with R --with-indices ai   &&
${hirata} \
  -f L2.in \
  -o ${folder}/L2HR2_from_L2.cpp \
  --prepend 'energy[""] = ' --contract-with R --with-indices abij &&
${hirata} \
  -f R1.in \
  -o ${folder}/L1HR1_from_R1.cpp \
  --prepend 'energy[""] = ' --contract-with L --with-indices ia   &&
${hirata} \
  -f R2.in \
  -o ${folder}/L2HR2_from_R2.cpp \
  --prepend 'energy[""] = ' --contract-with L --with-indices ijab

cat ${folder}/L1HR1_from_L1.cpp ${folder}/L2HR2_from_L2.cpp > ${folder}/LHR_from_L.cpp
cat ${folder}/L1HR1_from_R1.cpp ${folder}/L2HR2_from_R2.cpp > ${folder}/LHR_from_R.cpp

sed "/\/\//d; /^$/d" ${folder}/LHR_from_L.cpp > ${folder}/LHR_from_L_clean.cpp
sed "/\/\//d; /^$/d" ${folder}/LHR_from_R.cpp > ${folder}/LHR_from_R_clean.cpp

#vim-run: bash %

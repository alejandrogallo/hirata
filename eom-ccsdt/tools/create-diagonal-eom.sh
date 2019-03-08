#! /usr/bin/env bash

SCRIPT_DIR=$(readlink -f $(dirname $0))
hirata=hirata

if [[ -z $1 ]]; then
  echo "Usage: $(basename $0) <folder-with-L-and-R-equations>"
  exit 1
fi

equations_folder=$1
cd ${equations_folder}

folder=diagonal
mkdir -p ${diagonal_file}

set -eux

${hirata} \
  -f L1.in \
  -o ${folder}/L1HR1_from_L1.cpp \
  --prepend 'energy[""] = ' --contract-with R --with-indices ai   &&
${hirata} \
  -f L2.in \
  -o ${folder}/L2HR2_from_L2.cpp \
  --prepend 'energy[""] = ' --contract-with R --with-indices abij &&
${hirata} \
  -f L3.in \
  -o ${folder}/L3HR3_from_L3.cpp \
  --prepend 'energy[""] = ' --contract-with R --with-indices abcijk &&


${hirata} \
  -f R1.in \
  -o ${folder}/L1HR1_from_R1.cpp \
  --prepend 'energy[""] = ' --contract-with L --with-indices ia   &&
${hirata} \
  -f R2.in \
  -o ${folder}/L2HR2_from_R2.cpp \
  --prepend 'energy[""] = ' --contract-with L --with-indices ijab &&
${hirata} \
  -f R3.in \
  -o ${folder}/L3HR3_from_R3.cpp \
  --prepend 'energy[""] = ' --contract-with L --with-indices ijkabc


cat \
  ${folder}/L1HR1_from_L1.cpp \
  ${folder}/L2HR2_from_L2.cpp \
  ${folder}/L3HR3_from_L3.cpp \
  > ${folder}/LHR_from_L.cpp
cat \
  ${folder}/L1HR1_from_R1.cpp \
  ${folder}/L2HR2_from_R2.cpp \
  ${folder}/L3HR3_from_R3.cpp \
  > ${folder}/LHR_from_R.cpp

#Up to here it is the contracted code, now we remove Onebody H twobody
#terms etc...

for file in ${folder}/LHR_from_L.cpp ${folder}/LHR_from_R.cpp; do
  echo ${file}
  file_clean=${folder}/$(basename ${file} .cpp)_clean.cpp
  diagonal_file=${folder}/$(basename ${file} .cpp)_diagonal.cpp
  diagonal_file_clean=${folder}/$(basename ${file} .cpp)_diagonal_clean.cpp
  echo > ${diagonal_file}
  cat ${file} | grep Lia   | grep Rai   >> ${diagonal_file}
  cat ${file} | grep Lijab | grep Rabij >> ${diagonal_file}
  # Cleaning comments
  sed "/\/\//d; /^$/d" ${diagonal_file} > ${diagonal_file_clean}
  sed "/\/\//d; /^$/d" ${file} > ${file_clean}
done

#vim-run: bash % eom-ccsd/

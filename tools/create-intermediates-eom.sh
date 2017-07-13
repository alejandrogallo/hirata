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

folder=intermediates

set -x

${hirata} --fock \
  -f L1.in \
  -o ${folder}/L1H.cpp \
  --with-intermediates LH \
  --with-indices ia   &&
${hirata} --fock \
  -f L2.in \
  -o ${folder}/L2H.cpp \
  --with-intermediates LH \
  --with-indices ijab &&
${hirata} --fock \
  -f R1.in \
  -o ${folder}/HR1.cpp \
  --with-intermediates HR \
  --with-indices ai   &&
${hirata} --fock \
  -f R2.in \
  -o ${folder}/HR2.cpp \
  --with-intermediates HR \
  --with-indices abij

for out in ${folder}/* ; do
  sed "/\/\//d; /^$/d" ${out} > ${folder}/$(basename ${out} .cpp)-no-comment.cpp
done

#cat ${folder}/L1HR1_from_L1.cpp ${folder}/L2HR2_from_L2.cpp > ${folder}/LHR_from_L.cpp
#cat ${folder}/L1HR1_from_R1.cpp ${folder}/L2HR2_from_R2.cpp > ${folder}/LHR_from_R.cpp

#sed "/\/\//d; /^$/d" ${folder}/LHR_from_L.cpp > ${folder}/LHR_from_L_clean.cpp
#sed "/\/\//d; /^$/d" ${folder}/LHR_from_R.cpp > ${folder}/LHR_from_R_clean.cpp

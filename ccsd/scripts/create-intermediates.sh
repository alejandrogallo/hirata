#! /usr/bin/env bash

SCRIPT_DIR=$(readlink -f $(dirname $0))
hirata=${SCRIPT_DIR}/../../hirata.py

equations_folder=$1
cd ${equations_folder}

cat <<EOF
SCRIPT_DIR       = ${SCRIPT_DIR}
hirata           = ${hirata}
equations_folder = ${equations_folder}
EOF

if [[ ! -f ${hirata} ]]; then
  echo "You need the hirata.py script to continue"
  exit 1
fi

if [[ -z $1 ]]; then
  echo "Usage: $(basename $0) <folder-with-L-and-R-equations>"
  exit 1
fi


folder=intermediates

set -x

${hirata} --fock \
  -f T1.in \
  -o ${folder}/X1.cpp \
  --with-intermediates X \
  --with-indices ai   &&

${hirata} --fock \
  -f T2.in \
  -o ${folder}/X2.cpp \
  --with-intermediates X \
  --with-indices abij

#for out in ${folder}/* ; do
  #sed "/\/\//d; /^$/d" ${out} > ${folder}/$(basename ${out} .cpp)-no-comment.cpp
#done

#cat ${folder}/L1HR1_from_L1.cpp ${folder}/L2HR2_from_L2.cpp > ${folder}/LHR_from_L.cpp
#cat ${folder}/L1HR1_from_R1.cpp ${folder}/L2HR2_from_R2.cpp > ${folder}/LHR_from_R.cpp

#sed "/\/\//d; /^$/d" ${folder}/LHR_from_L.cpp > ${folder}/LHR_from_L_clean.cpp
#sed "/\/\//d; /^$/d" ${folder}/LHR_from_R.cpp > ${folder}/LHR_from_R_clean.cpp

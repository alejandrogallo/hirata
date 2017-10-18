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

folder=factors
mkdir -p ${folder}

equations=$(ls *.in)

set -x

for equation in ${equations} ; do
${hirata} --fock \
  -f ${equation} \
  --python-tuples-out ${folder}/$(basename ${equation} .in).py
done

exit 0

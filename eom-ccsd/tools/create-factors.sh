#! /usr/bin/env bash

SCRIPT_DIR=$(readlink -f $(dirname $0))
hirata=hirata

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
  ${hirata} \
    -f ${equation} \
    --python-tuples-out ${folder}/$(basename ${equation} .in).py
done

all_equations_file=${folder}/equations.py
py_files=$(ls ${folder}/*.py)

echo "[" > ${all_equations_file}
for equation in ${py_files}; do
  sed "s/^.*$/&,/" ${equation} >> ${all_equations_file}
done
echo "]" >> ${all_equations_file}

exit 0

#! /usr/bin/env bash

if [[ -z $@ ]]; then
  echo "Usage: $(basename $0) hirata-source.in"
  exit 1
fi

grep v $@         |
sed "s/.*v/v/"    |
sed "s/\*.*$//"   |
sed "s/[0-9]//g " |
sort              |
uniq

#vim-run: bash %

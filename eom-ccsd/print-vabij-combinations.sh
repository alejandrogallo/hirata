#! /usr/bin/env bash

grep v *.in       |
sed "s/.*v/v/"    |
sed "s/\*.*$//"   |
sed "s/[0-9]//g " |
sort              |
uniq

#vim-run: bash %

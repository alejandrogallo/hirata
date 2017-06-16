#! /usr/bin/env bash

in=${1:-LHR.cpp}

sed "
  s_//.*__;
  /^$/d
  s/ *$//
  s/ \[/[/g
  s/$/;/
  s/^/energy[\"\"] += /
  s/V..../(*&)/
  s/Lai/(*&)/
  s/Rai/(*&)/
  s/\s\s\s*/ /g
" ${in}


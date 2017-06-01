#! /usr/bin/env bash

in_files=(*.in)

for inf in ${in_files[@]} ; do
  echo ${inf}
  out=$(basename ${inf} .in).out
  cpp=$(basename ${inf} .in).cpp
  cp ${inf} ${out}
  echo "Comments ..."
  sed -i "
    s/^.*/\/\/&/;
    p;
    s/\/\///;
  " ${out}

  echo "Indices ..."
  sed -i "
  /\/\// ! {
    s/p1/a,/g;
    s/p2/b,/g;
    s/p3/c,/g;
    s/p4/d,/g;
    s/p5/e,/g;
    s/p6/f,/g;
    s/p7/g,/g;
    s/p8/h,/g;
  }
  " ${out}

  sed -i "
  /\/\// ! {
    s/h1/i,/g;
    s/h2/j,/g;
    s/h3/k,/g;
    s/h4/l,/g;
    s/h5/m,/g;
    s/h6/n,/g;
    s/h7/o,/g;
    s/h8/p,/g;
  }
  " ${out}

  echo "Projector ..."
  sed -i "
  /\/\// ! {
    s/P(\([^)]*\))/P{\1}/g
  }
  " ${out}

  echo "Parenthesis ..."
  sed -i "
  /\/\// ! {
    s/[^P]( /[\"/g;
    s/, )/\"]/g;
  }
  " ${out}

  echo "Variables ..."
  sed -i "
  /\/\// ! {
    s/v/Vabij/g;
    s/t\(\[... ..\]\)/Tai\1/g;
    s/y\(\[... ..\]\)/Lai\1/g;
    s/x\(\[... ..\]\)/Rai\1/g;
    s/t/Tabij/g;
    s/y/Labij/g;
    s/x/Rabij/g;
    s/f\[/Fai[/g;
  }
  " ${out}

  echo "Comas ..."
  sed -i "
  /\/\// ! {
    s/, //g
  }
  " ${out}

  echo "Sums ..."
  sed -i "
  /\/\// ! {
    s/Sum[^ ]* \*//g
  }
  " ${out}

  echo "Constants ..."
  sed -i "
  /\/\// ! {
    s/\[ /( /
    s/\] /) /
  }
  " ${out}

  sed "
  /\/\//d
  " ${out} > ${cpp}

  #echo "// vim: ft=cpp" >> ${out}

  column -t -s \* -o \* ${out} > temp
  cp temp ${out}
  column -t -s \* -o \* ${cpp} > temp
  cp temp ${cpp}

done

vi +"au BufReadPre,BufReadPost,VimEnter * set ft=cpp" *.out *.cpp

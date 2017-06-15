#! /usr/bin/env bash

print_with_deleted_comments() {
  sed "
  /\/\//d
  " ${1}
}

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

  echo "Constants parentheses ..."
  sed -i "
  /\/\// ! {
    s/\[ /( /
    s/\] /) /
  }
  " ${out}

  echo "Permutation operator ..."
  sed -i "
  /\/\// ! {
    s/\s\([a-z]\+\)=>/\"\1\"=>/g
    s/=>\s*\([a-z]\+\)\s*/=>\"\1\"/g
    s/=>/, /g
    s/{/(/g
    s/}/)/g
  }
  " ${out}

  echo "Change Fai into Fij or Fab depending on the indices"
  sed -i "
  /\/\// ! {
    /Fai/s/Fai\[\"\([a-h][a-h]\)\"\]/Fab[\1]/g;
    /Fai/s/Fai\[\"\([i-o][i-o]\)\"\]/Fij[\1]/g;
  }
  " ${out}

  echo "Muting remaining Fai because of HF orbitals"
  sed -i "
  /\/\// ! {
    /Fai/s_^_//_
  }
  " ${out}

  print_with_deleted_comments ${out} > ${cpp}

  #echo "// vim: ft=cpp" >> ${out}

  column -t -s \* -o \* ${out} > temp
  cp temp ${out}
  column -t -s \* -o \* ${cpp} > temp
  cp temp ${cpp}

  echo "CCSD"
  mkdir -p ccsd
  cp ${cpp} ccsd/

  echo "CCD"
  mkdir -p ccd
  sed "
    /Tai/d
  " ${cpp} > ccd/$(basename ${cpp} .cpp).cpp

  echo "CCD-EOMD"
  mkdir -p ccd-eomd
  sed "
    /Tai/d
    /Lai/d
    /Rai/d
  " ${cpp} > ccd-eomd/$(basename ${cpp} .cpp).cpp

  echo "Clean up"
  rm temp
  rm ${cpp}

done

#vi +"au BufReadPre,BufReadPost,VimEnter * set ft=cpp" *.out *.cpp
#vi +"au BufReadPre,BufReadPost,VimEnter * set ft=cpp" *ccd.cpp

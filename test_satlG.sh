#!/bin/bash

function test(){

  for file in `ls -a "$1"`
  do
      if [ -d "$1/$file" ]
      then
          if [[ $file != '.' && $file != '..' ]]
          then
              test "$1/$file"
          fi
      else
          echo "$1/$file" >> testResult_for_SATLikeHFCRP-C.txt
          ./HFCRP-C "$1/$file" >> testResult_for_SATLikeHFCRP-C.txt
      fi
  done
}

INIT_PATH1="../../SATSolvers/extracted_maxsat_instances/MS18"
INIT_PATH2="../../SATSolvers/extracted_maxsat_instances/MS19"
INIT_PATH3="../../SATSolvers/extracted_maxsat_instances/MS20"
INIT_PATH4="../../SATSolvers/extracted_maxsat_instances/MS21"
#INIT_PATH5="../../SATSolvers/extracted_maxsat_instances/MS22"

for INIT_PATH in $INIT_PATH1 $INIT_PATH2 $INIT_PATH3 $INIT_PATH4;  do
  test $INIT_PATH
done
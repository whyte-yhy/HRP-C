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
          echo "$1/$file" >> testResult_for_SATLike_GHRP.txt
          ./SATLG_HRP "$1/$file" >> testResult_for_SATLike_GHRP.txt
      fi
  done
}


INIT_PATH1="../../SATSolvers/extracted_maxsat_instances/MS19"
INIT_PATH2="../../SATSolvers/extracted_maxsat_instances/MS20"
INIT_PATH3="../../SATSolvers/extracted_maxsat_instances/MS21"

for INIT_PATH in $INIT_PATH1 $INIT_PATH2 $INIT_PATH3; do
  test $INIT_PATH
done
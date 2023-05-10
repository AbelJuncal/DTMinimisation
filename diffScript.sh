#!/bin/bash

dirsource="PyOutput/"
dirdestination="prolog/prologOutput/"

for filename in $(ls $dirsource)
do 
    inputname=$dirsource$filename
    outputname=$dirdestination$filename
    echo Comparando $inputname with $outputname
    diff <(sort $inputname) <(sort $outputname)
done
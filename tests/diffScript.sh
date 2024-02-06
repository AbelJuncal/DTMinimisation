#!/bin/bash

echo -n "Folder test:"
read testFolder

dirsource="tests/$testFolder/PyOutput/"
dirdestination="tests/$testFolder/prologOutput/"

#dirsource="PyOutput/"
#dirdestination="prologOutput/"

for filename in $(ls $dirsource)
do 
    inputname=$dirsource$filename
    outputname=$dirdestination$filename
    echo Comparando $inputname with $outputname
    diff <(sort $inputname) <(sort $outputname)
done

#!/bin/bash

echo -n "Folder test:"
read testFolder

dirsource="tests/$testFolder/GeneratedExamples/"
dirdestination="tests/$testFolder/prologOutput/"

direxecutable="prolog/"

for filename in $(ls $dirsource)
do
    echo $filename
    inputname=$dirsource$filename
    outputname=$dirdestination$filename
    ./${direxecutable}mindt $inputname > $outputname
done
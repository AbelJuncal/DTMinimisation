#!/bin/bash

dirsource="GeneratedExamples/"
dirdestination="prologOutput/"
direxecutable="prolog/"

for filename in $(ls $dirsource)
do
    echo $filename
    inputname=$dirsource$filename
    outputname=$dirdestination$filename
    ./${direxecutable}mindt $inputname > $outputname
done
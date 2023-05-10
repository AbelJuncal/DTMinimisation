#!/bin/bash

dirsource="GeneratedExamples/"
dirdestination="prologOutput/"

for filename in $(ls $dirsource)
do 
    inputname=$dirsource$filename
    outputname=$dirdestination$filename
    ./mindt $inputname > $outputname
done
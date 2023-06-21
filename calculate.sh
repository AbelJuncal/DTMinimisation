#!/bin/bash

dirsource="GeneratedExamples/"
output_file="times/pythonTimes.txt"

for i in {1..5}; do
for filename in $(ls $dirsource)
do
    python3 calculatefc.py $filename
    echo $filename 
done
done
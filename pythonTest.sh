#!/bin/bash

dirsource="GeneratedExamples/"
output_file="times/pythonTimes.txt"

for i in {1..5}; do
for filename in $(ls $dirsource)
do
    execution_time=$( { time python3 main.py $filename ; } 2>&1 | grep "real" | awk '{print $2}' )
    echo $filename 
    #/usr/bin/time -o kk.txt python3 main.py $filename
    echo "$filename.$execution_time" >> "$output_file"
done
done
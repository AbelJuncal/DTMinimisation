#!/bin/bash

echo -n "Folder test:"
read testFolder

dirsource="tests/$testFolder/GeneratedExamples/"
output_file="tests/$testFolder/times/pythonTimes.txt"

for i in {1..5}; do
for filename in $(ls $dirsource)
do
    execution_time=$(timeout 120 bash -c "execution_time=\$( { time python3 main.py $filename ; } 2>&1 | grep 'real' | awk '{print \$2}' ); echo \$execution_time")
    echo $filename 
    #/usr/bin/time -o kk.txt python3 main.py $filename
    echo "$filename.$execution_time" >> "$output_file"
done
done
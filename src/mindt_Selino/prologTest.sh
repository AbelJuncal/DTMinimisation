#!/bin/bash

echo -n "Folder test:"
read testFolder

dirsource="tests/$testFolder/GeneratedExamples/"
output_file="tests/$testFolder/times/prologTimes.txt"


direxecutable="prolog/"

for i in {1..5}; do
for filename in $(ls $dirsource)
do
    echo $filename
    inputname=$dirsource$filename
    execution_time=$(timeout 120 bash -c "execution_time=\$( { time ${direxecutable}mindt $inputname ; } 2>&1 | grep 'real' | awk '{print \$2}' ); echo \$execution_time")
    echo "$filename.$execution_time" >> "$output_file"
done
done

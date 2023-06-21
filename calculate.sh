#!/bin/bash

echo -n "Folder test:"
read testFolder

dirsource="tests/$testFolder/GeneratedExamples/"

for i in {1..5}; do
for filename in $(ls $dirsource)
do
    echo $filename
    python3 calculatefc.py $testFolder $filename
done
done
#!/bin/bash

dirsource="GeneratedExamples/"

for filename in $(ls $dirsource)
do 
    python3 main.py $filename
done
#!/bin/bash

for i in {1..5}
do 
    echo "----- Day $i ----"
    cd day$i
    python3 script.py
    cd ..
done
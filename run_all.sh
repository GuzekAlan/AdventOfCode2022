#!/bin/bash

for i in {1..4}
do 
    echo "----- Day $i ----"
    cd day$i
    python3 script.py
    cd ..
done
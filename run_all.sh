#!/bin/bash

for i in {1..4}
do 
    echo "----- Day $i ----"
    cd d$i
    python3 script.py
    cd ..
done
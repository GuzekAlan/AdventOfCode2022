#!/bin/python3

def isElapsing(e1, e2):
    e1b, e1e = map(int, e1.split('-'))
    e2b, e2e = map(int, e2.split('-'))
    res = 0
    if e1b >= e2b and e1e <= e2e or e1b <= e2b and e1e >= e2e:
        res = 1
    return res

def isElapsing2(e1, e2):
    e1b, e1e = map(int, e1.split('-'))
    e2b, e2e = map(int, e2.split('-'))
    x = [i for i in range(e1b, e1e+1) if i in range(e2b, e2e+1)]
    return int(bool(x))

with open('data.txt', 'r') as file:
    lines = file.read().splitlines()
    count = 0
    count2 = 0
    for line in lines:
        count += isElapsing(*line.split(','))
        count2 += isElapsing2(*line.split(','))

print(count)
print(count2)
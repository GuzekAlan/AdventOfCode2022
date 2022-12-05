#!/bin/python3

from string import ascii_lowercase, ascii_uppercase

def getPoint(c):
    return ascii_lowercase.index(c)+1 if c.islower() else ascii_uppercase.index(c)+27

def p1(lines):
    points = 0
    for line in lines:
        left = line[:len(line)//2]
        right = line[len(line)//2:]
        both = [c for c in left if c in right][0]
        points += getPoint(both)
    return points

def p2(lines):
    points = 0
    for i in range(len(lines)//3):
        badge = [c for c in lines[i*3] if ((c in lines[i*3+1]) and (c in lines[i*3+2]))][0]
        points += getPoint(badge)
    return points


with open('data.txt', 'r') as file:
    lines = file.read().splitlines()
    print(p1(lines))
    print(p2(lines))
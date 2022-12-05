#!/bin/python3

def elves():
    elves = []
    with open('data.txt') as file:
        lines = file.read().splitlines()
        temp = 0
        for line in lines:
            if line == '':
                elves.append(temp)
                temp = 0
            else:
                temp += int(line)
        return elves
      
print(max(elves()))
print(sum(sorted(elves(), reverse=True)[:3]))
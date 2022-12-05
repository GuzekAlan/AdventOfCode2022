#!/bin/python3

def prepareData():
    with open('data.txt') as file:
        lines = file.read().splitlines()
        crates = lines[:8]
        moves = lines[11:]
        crateStacks = [[] for i in range(9)]
        commands = []
        for row in crates[::-1]:
            x = row.replace('[', '').replace('] ', ',').replace('    ', '-,').replace(']', '').split(',')
            for i, v in enumerate(x):
                if v != '-':
                    crateStacks[i].append(v)
        # print(crateStacks)
        for row in moves:
            commands.append(tuple(map(int, row.replace('move ', '').replace('from ', '').replace('to ', '').split(' '))))
        # print(commands)
        return crateStacks, commands
            
def main():
    crateStacks, commands = prepareData()
    for command in commands:
        count, fromStack, toStack = command
        print(count)
        crateStacks[toStack].append(crateStacks[fromStack][-count:])
        crateStacks[fromStack] = crateStacks[fromStack][:-count]
    for stack in crateStacks:
        print(stack[-1])
        
main()
#!/bin/python3

def printMatrix(matrix):
    print('\n'.join([str(i+1)+ ' ' + ' '.join([str(cell) for cell in row]) for i, row in enumerate(matrix)]))

def prepareData():
    with open('data.txt') as file:
        lines = file.read().splitlines()
        crates = lines[:8]
        moves = lines[10:]
        crateStacks = [[] for i in range(9)]
        commands = []
        for row in crates[::-1]:
            x = row.replace('[', '').replace('] ', ',').replace('    ', '-,').replace(']', '').split(',')
            for i, v in enumerate(x):
                if v != '-':
                    crateStacks[i].append(v)
        crateStacks[8].pop()    # cleaning this input is horror
        for row in moves:
            commands.append(tuple(map(int, row.replace('move ', '').replace('from ', '').replace('to ', '').split(' '))))
        return crateStacks, commands
            
def crane_one():
    crateStacks, commands = prepareData()
    for command in commands:
        count, fromStack, toStack = map(sum, zip(command, (0, -1, -1)))
        for _ in range(count):
            crateStacks[toStack].append(crateStacks[fromStack].pop())
    printMatrix(crateStacks)
    for stack in crateStacks:
        print(stack[-1], end='')
    print()
    
def crane_two():
    crateStacks, commands = prepareData()
    for command in commands:
        count, fromStack, toStack = map(sum, zip(command, (0, -1, -1)))
        crateStacks[toStack].extend(crateStacks[fromStack][-count:])
        crateStacks[fromStack] = crateStacks[fromStack][:-count]
    printMatrix(crateStacks)
    for stack in crateStacks:
        print(stack[-1], end='')
    print()   

def main():
    crane_one()
    crane_two()
    
main()
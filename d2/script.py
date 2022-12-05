#!/bin/python3

# A       B       C
# X       Y       Z
# Rock    Paper   Scissors 

oponent_dict = {'A': 1, 'B': 2, 'C': 3}
player_dict = {'X': 1, 'Y': 2, 'Z': 3}
move_dict = {'X': 0, 'Y': 3, 'Z': 6}


def calculate_score(oponent, player):
    o = oponent_dict[oponent]
    p = player_dict[player]
    if o == p:
        return 3 + p
    if o == 1 and p == 2 or o == 2 and p == 3 or o == 3 and p == 1:
        return 6 + p
    return p


def calculate_points_2(oponent, move):
    o = oponent_dict[oponent]
    m = move_dict[move]
    if m == 0:
        p = (o+1)%3+1
    if m == 3:
        p = o
    if m == 6:
        p = (o)%3+1
    return p + m

with open('data.txt', 'r') as file:
  points = 0
  points2 = 0
  input_data = file.read().splitlines()
  for i in input_data:
    points += calculate_score(*(i.split(' ')))
    points2 += calculate_points_2(*(i.split(' ')))

print(f'{points=}')
print(f'{points2=}')
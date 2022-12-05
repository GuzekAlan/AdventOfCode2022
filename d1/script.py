

elves = []
with open('data.txt') as file:
  temp = 0
  for line in file:
    val = line.strip('\n')
    if val == '':
      elves.append(temp)
      temp=0
    else:
      temp += int(val)
      
print(sum(sorted(elves, reverse=True)[:3]))
# Databricks notebook source
import requests
import numpy as np
import matplotlib.pyplot as plt

day = 23

small = True
smallest = False

if small:
  if smallest:
    with open('input23_smaller.txt') as f:
      data = f.read().splitlines() 
  else:
    with open('input23_small.txt') as f:
      data = f.read().splitlines()
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.splitlines()
      
mappie = [x for x in data]

# COMMAND ----------

elves = {}
elf_n = 0
for row,line in enumerate(mappie):
  for col,character in enumerate(line):
     
    if character == '#':
      
      elf_n += 1
      elf = {}
      elf['name'] = elf_n
      elf['pos'] = col+row*1j
      elf['proposed'] = None
      elf['new_pos'] = None
      elf['neighboring'] = None
      elves[elf_n] = elf


# COMMAND ----------

direction_north = ['north',0-1j ,[1-1j,0-1j,-1-1j]]
direction_south = ['south',0+1j ,[1+1j,0+1j,-1+1j]]
direction_west  = ['west',-1+0j,[-1+1j,-1,-1-1j]]
direction_east  = ['east',1+0j ,[1-1j,1-0j,1+1j]]

direction = direction_north + direction_south + direction_west + direction_east


# COMMAND ----------

adjacent = [0-1j,1-1j,1,1+1j,0+1j,-1+1j,-1,-1-1j]

def get_proposed_position(elf):
  elf['proposed'] = None
  adjacent_pos = [elf['pos'] + x for x in adjacent]
  other_elves = [elves[x]['pos'] for x in list(elves.keys()) if x!= elf['name']]
  for x in adjacent_pos:
    if x in other_elves:        
      if set([elf['pos'] + x for x in direction[2]]).intersection(set(other_elves)) == set():
        elf['proposed'] = elf['pos'] + direction[1]
      elif set([elf['pos'] + x for x in direction[5]]).intersection(set(other_elves)) == set():
        elf['proposed'] = elf['pos'] + direction[4]
      elif set([elf['pos'] + x for x in direction[8]]).intersection(set(other_elves)) == set():
        elf['proposed'] = elf['pos'] + direction[7]
      elif set([elf['pos'] + x for x in direction[11]]).intersection(set(other_elves)) == set():
        elf['proposed'] = elf['pos'] + direction[10]
      break        
  return elf
  

# COMMAND ----------

round = 0
moved = True
while moved:
  print(round)
  round +=1
  moved = False
  #round 1: get proposed position
  for elf in elves:

    elves[elf] = get_proposed_position(elves[elf])

  #round 2: check if proposed position is free
  for elf in elves:
    other_elves = [elves[x]['proposed'] for x in list(elves.keys()) if x!= elves[elf]['name']]
    if set([elves[elf]['proposed']]).intersection(set(other_elves)) == set():
      elves[elf]['pos'] = elves[elf]['proposed']
      moved = True
  direction = direction[3:12] + direction[0:3]
  if round == 10:
    min_col = min([elves[x]['pos'].real for x in elves])
    max_col = max([elves[x]['pos'].real for x in elves])+1
    min_row = min([elves[x]['pos'].imag for x in elves])
    max_row = max([elves[x]['pos'].imag for x in elves])+1

    print(f'Answer 1: {int(((max_col - min_col) * (max_row - min_row)) -len(elves))}')
        
    cave = np.zeros((int(max_row-min_row),int(max_col-min_col)))
    for elf in elves:
      cave[int(elves[elf]['pos'].imag)-int(min_row)][int(elves[elf]['pos'].real)-int(min_col)] = 1

    fig, ax = plt.subplots(figsize=(10,10))
    im = plt.imshow(cave)
    plt.show()

print(f'Answer 2: {round}')  #about 1000 rounds
  

# COMMAND ----------

min_col = min([elves[x]['pos'].real for x in elves])
max_col = max([elves[x]['pos'].real for x in elves])+1
min_row = min([elves[x]['pos'].imag for x in elves])
max_row = max([elves[x]['pos'].imag for x in elves])+1

cave = np.zeros((int(max_row-min_row),int(max_col-min_col)))
for elf in elves:
  cave[int(elves[elf]['pos'].imag)-int(min_row)][int(elves[elf]['pos'].real)-int(min_col)] = 1

fig, ax = plt.subplots(figsize=(10,10))
im = plt.imshow(cave)
plt.show()



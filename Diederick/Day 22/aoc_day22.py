# Databricks notebook source
import re
import requests
import numpy as np
import matplotlib.pyplot as plt

day = 22
small = False

if small:
  with open('input22_small.txt') as f:
    data = f.read().split('\n\n')
else:
  cookies = {'session': '53616c7465645f5f1f7b2f796a4556ee8ae4c0b6a01f75fb54e82194d3f8815048534e4e315ca6c5ee07402b983e327fc6b79a28b237c72ed1ea6f6157e38e1d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.split('\n\n')


field = data[0].splitlines()
path = data[1]

pattern = r'R|L'
turn = re.findall(pattern,path)
steps = list(map(int,re.split('R|L',path)))


# COMMAND ----------

open_tiles = set()
walls = set()

for row_i,row in enumerate(field):
  for col_j,col in enumerate(row):
    if col == '.':
      open_tiles.add(col_j+1+(row_i+1)*1j)

    elif col == '#':
      walls.add(col_j+1+(row_i+1)*1j)

# COMMAND ----------

columns = int(max([x.real for x in open_tiles]))
rows = int(max([x.imag for x in open_tiles]))
field_map = np.zeros((rows,columns))

for tile in open_tiles:
#   print(int(tile.real-1),int(tile.imag-1))
  field_map[int(tile.imag-1)][int(tile.real-1)] = 1
for wall in walls:
#   print(int(tile.real-1),int(tile.imag-1))
  field_map[int(wall.imag-1)][int(wall.real-1)] = 2
  

fig, ax = plt.subplots(figsize=(10,10))
im = plt.imshow(field_map)
plt.show()

# COMMAND ----------

def change_dir(dir,turn):
  if turn == 'R':
    if dir == 1+0j:  #right
      dir = 0+1j #'down'
    elif dir == 0+1j: #down
      dir = -1+0j # 'left'
    elif dir == -1+0j: #'left'
      dir = 0-1j     #'up'
    elif dir == 0-1j:# 'up'
      dir = 1+0j #'right'
  else:
    if dir == 1+0j:  #right
      dir = 0-1j #'up'
    elif dir == 0+1j: #down
      dir =  1+0j #'right'
    elif dir == -1+0j: #'left'
      dir = 0+1j#'down'
    elif dir == 0-1j:# 'up'
      dir = -1+0j #'left'
  return dir

# COMMAND ----------

def walk(pos,dir):
  new_pos = pos + dir
  if (new_pos not in open_tiles.union(walls)) and dir.real == -1 :  #move to left out of bounds / empty    1+7j
    new_real = max([x.real for x in open_tiles.union(walls) if x.imag == new_pos.imag])
    new_pos = new_real + new_pos.imag*1j
  if (new_pos not in open_tiles.union(walls)) and dir.real == 1:    #move to right out of bounds / empty   16+10j
    new_real = min([x.real for x in open_tiles.union(walls) if x.imag == new_pos.imag])
    new_pos = new_real + new_pos.imag*1j
  if (new_pos not in open_tiles.union(walls)) and dir.imag == -1:    #move up out of bounds / empty    9+1j
    new_imag = max([x.imag for x in open_tiles.union(walls) if x.real == new_pos.real])
    new_pos = new_pos.real + new_imag*1j
  if (new_pos not in open_tiles.union(walls)) and dir.imag == 1:    #move down out of bounds / empty   9+12j
    new_imag=min([x.imag for x in open_tiles.union(walls) if x.real == new_pos.real]) 
    new_pos = new_pos.real + new_imag*1j
  if new_pos in walls:
      new_pos = pos
  return new_pos

# COMMAND ----------

def walk_cube(pos,dir):
  new_pos = pos + dir
  new_dir = dir
  if (new_pos not in open_tiles.union(walls)) and dir.real == -1 :  #move to left out of bounds / empty    1+7j
    if (1<= pos.imag <= 50):
#       print('go from 1 to 5')
      new_pos = 1 + (151 - pos.imag)*1j
      new_dir = 1
    elif (51<= pos.imag <= 100):
#       print('go from 3 to 5')
      new_pos = (pos.imag - 50) + 101*1j
      new_dir = 1j
    elif (101<= pos.imag <= 150):
#       print('go from 5 to 1')
      new_pos = 51 + (151-pos.imag)*1j
      new_dir = 1
    elif (151 <= pos.imag <= 200):
#       print('go from 6 to 1')
      new_pos = (pos.imag-100)+1j
      new_dir = 1j
  if (new_pos not in open_tiles.union(walls)) and dir.real == 1:   #move to right out of bounds / empty   16+10j
    if (1<= pos.imag <= 50):
#       print('go from 2 to 4')
      new_pos = 100 + (151-pos.imag)*1j
      new_dir = -1
    elif (51<= pos.imag <= 100):
#       print('go from 3 to 2')
      new_pos = (pos.imag+50)+50*1j
      new_dir = -1j
    elif (101<= pos.imag <= 150):
#       print('go from 4 to 2')
      new_pos = 150+(151-pos.imag)*1j
      new_dir = -1
    elif (151 <= pos.imag <= 200):
#       print('go from 6 to 4')
      new_pos = pos.imag - 100 + 150*1j
      new_dir = -1j
  if (new_pos not in open_tiles.union(walls)) and dir.imag == -1:    #move up out of bounds / empty    9+1j
    if (1<= pos.real <= 50): 
#       print('go from 5 to 3')
      new_pos = 51 + (pos.real+50)*1j
      new_dir = 1
    elif (51<= pos.real <= 100):
#       print('go from 1 to 6')
      new_pos = 1+ (pos.real+100)*1j
      new_dir = 1
    elif (101<= pos.real <= 150):
#       print('go from 2 to 6')
      new_pos = pos.real -100 + 200*1j
      new_dir = -1j
  if (new_pos not in open_tiles.union(walls)) and dir.imag == 1:    #move down out of bounds / empty   9+12j
    if (1<= pos.real <= 50):
#       print('go from 6 to 2')
      new_pos = pos.real+100 + 1j
      new_dir = 1j
    elif (51<= pos.real <= 100):
#       print('go from 4 to 6')
      new_pos = 50+ (pos.real+100)*1j
      new_dir = -1
    elif (101<= pos.real <= 150):
#       print('go from 2 to 3')
      new_pos = 100 + (pos.real-50) * 1j
      new_dir = -1
  if new_pos in walls:
      new_pos = pos
      new_dir = dir
  return new_pos,new_dir

# COMMAND ----------

start_x =min([x.real for x in open_tiles if x.imag == 1])
start_y = min([x.imag for x in open_tiles if x.real == start_x])

pos = start_x + start_y*1j
field_map[int(pos.imag-1)][int(pos.real-1)] = 3
dir = 1+0j


for iter,part in enumerate(['part 1','part 2']):
  pos = start_x + start_y*1j
  dir = 1+0j
  for i,step_size in enumerate(steps):
    for _ in range(step_size):
        old_pos = pos
        if part == 'part 1':
          pos = walk(pos,dir)
        elif part == 'part 2':
          pos,dir = walk_cube(pos,dir) 
        if pos == old_pos:
          break
          
    if i < len(turn):    
      dir = change_dir(dir,turn[i])
      
  if dir == 1:
    facing = 0
  elif dir == 1j:
    facing = 1
  elif dir == -1:
    facing = 2
  elif dir == -1j:
    facing = 3
  
  print(f'Answer {part}: {int((1000*pos.imag) + (4*pos.real) + (facing))}')


# COMMAND ----------

fig, ax = plt.subplots(figsize=(10,10))
im = plt.imshow(field_map)
plt.show()

# Databricks notebook source
import pandas as pd
import datetime
import requests
import re
import numpy as np
import matplotlib.pyplot as plt

day = 17

small = False

if small:
  jets = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  jets = r.text.splitlines()[0]

jets
  


# COMMAND ----------

# horizontal - star - mirror L - vertical - square

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # By Diederick

# COMMAND ----------

def coordinates_shape(shape,highest_rock):
  if shape == "horizontal":
    coords = [[3,highest_rock+5],[4,highest_rock+5],[5,highest_rock+5],[6,highest_rock+5]]
  elif shape == "star":
    coords = [[3,highest_rock+6],[4,highest_rock+6],[5,highest_rock+6],[4,highest_rock+7],[4,highest_rock+5]]
  elif shape == "L":
    coords = [[3,highest_rock+5],[4,highest_rock+5],[5,highest_rock+5],[5,highest_rock+6],[5,highest_rock+7]]
  elif shape ==  "vertical":
    coords = [[3,highest_rock+8],[3,highest_rock+7],[3,highest_rock+6],[3,highest_rock+5]]
  elif shape == "square": 
    coords = [[3,highest_rock+6],[4,highest_rock+6],[3,highest_rock+5],[4,highest_rock+5]]
  
  return coords

coordinates_shape('star',0)


# COMMAND ----------

def check_valid_gravity(coords_before,stopped):
  coords_after = [[i[0],i[1]-1] for i in coords_before]
  check = True
#   print('falling')
  if any(coord in stopped for coord in coords_after):
#     print('crashing in falling')
    coords_after = coords_before
    check=False
  return coords_after,check

# COMMAND ----------

def check_valid_jetmove(jet,coords_before,stopped):
  if jet == '>':
    coords_after= [[i[0]+1,i[1]] for i in coords_before]
    if any(coord in stopped for coord in coords_after) or any(coords[0] == 8 for coords in coords_after):
      coords_after = coords_before
  elif jet == '<':
    coords_after= [[i[0]-1,i[1]] for i in coords_before]
    if any(coord in stopped for coord in coords_after) or any(coords[0] == 0 for coords in coords_after):
      coords_after = coords_before
      
  return coords_after
  

# COMMAND ----------

shapes = ['horizontal','star','L','vertical','square']
highest_rock = 0
jet_i = 0

bottom = []
for x in range(0,9):
  bottom.append([x,0])

stopped = []
stopped = stopped + bottom

for x in range(2022):
#   if x % 100 == 0:
#     stopped = stopped[-50:]
  if x % 10000 == 0:
    print(x)
  shape = shapes[x%5]
  moving = True
  coords = coordinates_shape(shape,highest_rock)
#   print(coords)
  while moving:
    # move down
    coords,check = check_valid_gravity(coords,stopped)

    if not check:
      moving = False
      stopped.extend(coords)
      highest_rock = max(highest_rock,max([i[1] for i in coords]))

      continue
    # jet
    jet= jets[jet_i]
    coords = check_valid_jetmove(jet,coords,stopped)
#     print(coords)
    jet_i +=1
    if jet_i == len(jets):
      jet_i = 0
  if x == 2021:
    print(f'Answer 1: {highest_rock}')

    
    

# COMMAND ----------

max_y = max([x[1] for x in stopped])
cave = np.zeros((max_y+1,9))

for rock in stopped:
  if rock in bottom:
    continue
  cave[rock[1],rock[0]] = 1

fig, ax = plt.subplots(figsize=(10,100))
im = plt.imshow(np.flipud(cave))
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # By Hyper Neutrino

# COMMAND ----------

rocks = [
  [0,1,2,3],
  [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
  [0, 1, 2, 2 + 1j, 2 + 2j],
  [0, 1j, 2j, 3j],
  [0,1,1j,1+1j]
]

jets_dir = [1 if x == ">" else -1 for x in jets]
solid = {x-1j for x in range(7)}
height = 0

rc = 0
ri = 0

rock = {x+2 + (height+3) * 1j for x in rocks[ri]}



while rc < 2022:
  for jet in jets_dir:
    moved = {x+jet for x in rock}
    if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
      rock = moved
    moved = {x-1j for x in rock}
    if moved & solid:
      solid |= rock
      rc += 1
      o = height
      height = max(x.imag for x in solid)+1
      if rc >= 2022:
        break
      ri = (ri+1)%5      
      rock = {x+2 + (height+3) * 1j for x in rocks[ri]}
    else:
      rock = moved

print(f'Answer 1:{int(height)}')

# COMMAND ----------

rocks = [
  [0,1,2,3],
  [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
  [0, 1, 2, 2 + 1j, 2 + 2j],
  [0, 1j, 2j, 3j],
  [0,1,1j,1+1j]
]

jets_dir = [1 if x == ">" else -1 for x in jets]
solid = {x-1j for x in range(7)}
height = 0

seen = {}

def summarize():
  o = [-20]*7
  
  for x in solid:
    r = int(x.real)
    i = int(x.imag)
    o[r] = max(o[r],i)
    
  top = max(o)
  return tuple(x - top for x in o)

 
rc = 0
ri = 0

rock = {x+2 + (height+3) * 1j for x in rocks[ri]}

T = 1000000000000
while rc < T:
  for ji,jet in enumerate(jets_dir):
    moved = {x+jet for x in rock}
    if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
      rock = moved
    moved = {x-1j for x in rock}
    if moved & solid:
      solid |= rock
      rc += 1
      o = height
      height = max(x.imag for x in solid)+1
      if rc >= T:
        break
      ri = (ri+1)%5      
      rock = {x+2 + (height+3) * 1j for x in rocks[ri]}
      key = (ji,ri,summarize())
      if key in seen:
        lrc,lh = seen[key]
        rem = T - rc
        rep = rem // (rc-lrc)
        offset = rep * (height-lh)
        rc += rep * (rc - lrc)
        seen = {}
      seen[key] = (rc,height)
    else:
      rock = moved

print(f'Answer 2: {int(height+offset)}')


# COMMAND ----------



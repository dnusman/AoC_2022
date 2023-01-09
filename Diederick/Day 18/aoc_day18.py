# Databricks notebook source
import pandas as pd
import datetime
import requests
import re
import numpy as np
import matplotlib.pyplot as plt

day = 18

small = False
smallest = False

if small:
  if smallest:
    data = ['1,1,1','2,1,1']
  else: 
    with open('input18_small.txt') as f:
      data = f.read().splitlines()
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.splitlines()

data

# COMMAND ----------

def edges(start_coord):
  x = start_coord[0]
  y = start_coord[1]
  z = start_coord[2]
  edges = []
  for i in range(2):
    for j in range(2):
      for k in range(2):
        edges.append([x+i,y+j,z+k])
  return edges

edges([2,1,1])

# COMMAND ----------

cubes = {}

for i,v in enumerate(data):
  cube = {}
  cube['starting_coord'] = list(map(int,v.split(',')))
  cube['edges'] = edges(cube['starting_coord'])
  cube['free_faces'] = 6
  cubes[i] = cube

cubes

# cubes = {1: {'starting_coord': [1,1,1], 'edges' : [[1, 1, 1],[1, 1, 2],[1, 2, 1],[1, 2, 2],[2, 1, 1],[2, 1, 2],[2, 2, 1],[2, 2, 2]], 'free_faces': 6},
#          2: {'starting_coord': [2,1,1], 'edges' : [[2, 1, 1],[2, 1, 2],[2, 2, 1],[2, 2, 2],[3, 1, 1],[3, 1, 2],[3, 2, 1],[3, 2, 2]], 'free_faces': 6}}

# cubes


# COMMAND ----------


connected = 0
for cube in cubes:
  wanted_keys = [x for x in list(cubes.keys()) if x!= cube]
  
  for other_cube in wanted_keys:
    connected = 0
    for edge in cubes[cube]['edges']:
      if edge in cubes[other_cube]['edges']:
        connected += 1    
      if connected == 4:
        cubes[cube]['free_faces'] -= 1
        break
        
ans_1 = 0
for i in cubes:
  ans_1 += cubes[i]['free_faces']
  
print(f'Answer 1: {ans_1}')
  

# COMMAND ----------

cubes

# COMMAND ----------

## all starting coords between min_x,max_x,min_y,max_y and min_z and max_z not in cubes['starting_coord']
## check if all vertices are in cubes['edges']
## you found trapped air

# COMMAND ----------

vertex_list = []
for x in cubes:
  for edge in cubes[x]['edges']:
    vertex_list.append(tuple(edge))

vertex_list

# COMMAND ----------

min_x = min([x[0] for x in vertex_list])
max_x = max([x[0] for x in vertex_list])
min_y = min([x[1] for x in vertex_list])
max_y = max([x[1] for x in vertex_list])
min_z = min([x[2] for x in vertex_list])
max_z = max([x[2] for x in vertex_list])

# print(min_x,max_x,min_y,max_y,min_z,max_z)

cubes_startingcoords = []
for x in cubes:
    cubes_startingcoords.append(tuple(cubes[x]['starting_coord']))

# print(cubes_startingcoords)

ans_2 = 0
possible_air = []
for x in range(min_x-1,max_x+2):
  for y in range(min_y-1,max_y+2):
    for z in range(min_z-1,max_z+2):
      #possible air droplet at starting_coord x,y,z
      if (x,y,z) in cubes_startingcoords:
        continue
      else:
        vertex_air = edges([x,y,z])
        vertex_found = 0
        for vertex in vertex_air:
          if tuple(vertex) in vertex_list:
            vertex_found +=1
          if vertex_found == 8:
#             print(x,y,z)
            ans_2 +=1
            
## this goes wrong for adjacent air bubbles        
print(ans_1 -ans_2*6)    



# COMMAND ----------

4244-(488*6)

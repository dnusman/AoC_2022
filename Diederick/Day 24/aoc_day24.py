# Databricks notebook source
import math
from collections import deque
import requests

small = False
smaller = False
day = 24

if small:
  if smaller:
    with open('input24_smaller.txt') as f:
      data = f.read().splitlines()
  else:  
    with open('input24_small.txt') as f:
      data = f.read().splitlines()
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.splitlines()
    
data

# COMMAND ----------

#left right up down
def move_blizzard(blizzards,r,c):
  left = set()
  for blizzard in blizzards[0]: #left
    if blizzard[1]-1 < 0:
      left.add((blizzard[0],c-1))
    else:
      left.add((blizzard[0],blizzard[1]-1))
  
  right = set()        
  for blizzard in blizzards[1]: #right
    if blizzard[1]+1 == c:
      right.add((blizzard[0],0))
    else:
      right.add((blizzard[0],blizzard[1]+1))
    
  up = set()
  for blizzard in blizzards[2]: #up
    if blizzard[0]-1 <0:
      up.add((r-1,blizzard[1]))
    else:
      up.add((blizzard[0]-1,blizzard[1]))
    
  down = set()  
  for blizzard in blizzards[3]: #down
    if blizzard[0]+1 == r:
      down.add((0,blizzard[1]))
    else:
      down.add((blizzard[0]+1,blizzard[1]))
    
  return(left,right,up,down)    

# COMMAND ----------

blizzards = tuple(set() for _ in range(4))

for r,line in enumerate(data[1:]):
  for c,item in enumerate(line[1:]):
    if item in "<>^v":
      blizzards["<>^v".find(item)].add((r, c))

queue = deque([(0, -1, 0,blizzards)])
seen = set()
target = (r, c - 1)

lcm = r * c // math.gcd(r, c)

#### GO FIRST TIME ####
while queue:
  time,cr,cc,old_blizzards = queue.popleft()
  time +=1
  
  new_blizzards = move_blizzard(old_blizzards,r,c)
  
  for dr,dc in ((0,1),(0,-1),(-1,0),(1,0),(0,0)):
    nr = cr + dr
    nc = cc + dc
        
    if (nr,nc) == target:
      print(f'Answer 1: {time}')
      queue = deque()
      break
    
    if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (-1, 0):
      continue
    
    if sum([(nr,nc) in setje for setje in new_blizzards]) >=1:
      continue
  
    else:
      key = (nr,nc,time%lcm)
      if key in seen:
        continue
        
      seen.add(key)
      queue.append((time,nr,nc,new_blizzards))

#### GO BACK ####
queue = deque([(time, r, c-1,new_blizzards)])
seen = set()
target_back = (-1,0)

while queue:

  time,cr,cc,old_blizzards = queue.popleft()
  time +=1 

  new_blizzards = move_blizzard(old_blizzards,r,c)
  
  for dr,dc in ((0,1),(0,-1),(-1,0),(1,0),(0,0)):
    nr = cr + dr
    nc = cc + dc
    
    if (nr,nc) == target_back:
      queue = deque()
      break
    
    if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (r, c-1):
      continue    

    if sum([(nr,nc) in setje for setje in new_blizzards]) >=1:
      continue
  
    else:
      key = (nr,nc,time%lcm)
      if key in seen:
        continue
        
      seen.add(key)
      queue.append((time,nr,nc,new_blizzards))
  

#### GO SECOND TIME ####

queue = deque([(time, -1, 0,new_blizzards)])
seen = set()
target = (r, c - 1)

while queue:
  time,cr,cc,old_blizzards = queue.popleft()
  time +=1
  new_blizzards = move_blizzard(old_blizzards,r,c)
  
  for dr,dc in ((0,1),(0,-1),(-1,0),(1,0),(0,0)):
    nr = cr + dr
    nc = cc + dc
    
    if (nr,nc) == target:
      print(f'Answer 2: {time}')
      queue = deque()
      break
    
    if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (-1, 0):
      continue
    
    if sum([(nr,nc) in setje for setje in new_blizzards]) >=1:
      continue
  
    else:
      key = (nr,nc,time%lcm)
      if key in seen:
        continue
        
      seen.add(key)
      queue.append((time,nr,nc,new_blizzards))


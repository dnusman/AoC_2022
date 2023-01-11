# Databricks notebook source
from collections import deque
import requests

day = 16
small = False

if small:
  with open('input16_small.txt') as f:
    data = f.read().splitlines()
else:
  cookies = {'session': '53616c7465645f5f1f7b2f796a4556ee8ae4c0b6a01f75fb54e82194d3f8815048534e4e315ca6c5ee07402b983e327fc6b79a28b237c72ed1ea6f6157e38e1d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.splitlines()

valves = {}
tunnels = {}
  
for line in data:
  line = line.strip()
  valve = line.split()[1]
  flow = line.split(';')[0].split('=')[1]
  targets = line.split(";")[1].split('to ')[1].split(' ',1)[1].split(', ')
  valves[valve] = int(flow)
  tunnels[valve] = targets

print("valves: ",valves)
print("tunnels: ",tunnels)
  

# COMMAND ----------

dists = {}
nonempty = []

for valve in valves:
  if valve != "AA" and not valves[valve]:
    continue
    
  if valve != 'AA':
    nonempty.append(valve)
    
  dists[valve] = {valve: 0,"AA": 0}
  
  visited = {valve}
  
  queue = deque([(0,valve)])
  
  while queue:
    distance,position = queue.popleft()
    
    for neighbour in tunnels[position]:
      if neighbour in visited:
        continue
      visited.add(neighbour)
      if valves[neighbour]:
        dists[valve][neighbour] = distance + 1
      queue.append((distance+1,neighbour))

  
  del dists[valve][valve]
  if valve != "AA":
    del dists[valve]['AA']

indices = {}

for index,element in enumerate(nonempty):
  indices[element] = index

cache  = {}

def dfs(time, valve, bitmask):
  if (time,valve,bitmask) in cache:
    return cache[(time,valve,bitmask)]
  
  maxval = 0
  
  for neighbour in dists[valve]:
    bit = 1 << indices[neighbour]
    if bitmask & bit:
      continue
    remtime = time - dists[valve][neighbour] - 1
    if remtime <= 0:
      continue
    maxval = max(maxval,dfs(remtime, neighbour, bitmask | bit ) + valves[neighbour]*remtime)
      
  cache[(time,valve,bitmask)] = maxval
  
  return maxval

print(f'Answer 1: {dfs(30,"AA",0)}')

b = (1<< len(nonempty)) - 1

m = 0

for i in range((b+1)//2):
  m = max(m,(dfs(26,"AA",i) + dfs(26,"AA",b^i)))
  
print(f'Answer 2: {m}')


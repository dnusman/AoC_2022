# Databricks notebook source
from collections import deque
import requests 

small = False
day = 20

if small:
  with open("input20_small.txt") as f:
    data = [int(x) for x in f.read().splitlines()]
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = [int(x) for x in r.text.splitlines()]


# COMMAND ----------

def mix(ind,enumerated):
  while enumerated[0][0] != ind:
    enumerated.rotate(-1)
  
  current_pair = enumerated.popleft()
  shift_by = current_pair[1]
  enumerated.rotate(-shift_by)
  enumerated.append(current_pair)
  
  return enumerated

def value_at_n(values,n):
  digit = (values.index(0)+n) % len(values)
  return values[digit]

# COMMAND ----------

rounds = [[1,1,1],[2,10,811589153]] #part / number of rounds / multiplication key

for round in rounds:
  new_data = [val*round[2] for val in data]
  enumerated = deque(list(enumerate(new_data.copy())))
  
  for _ in range(round[1]):
    for i in range(len(enumerated)):
      enumerated = mix(i,enumerated)

  ans = 0
  for n in [1000,2000,3000]:
    ans += value_at_n([val[1] for val in enumerated],n)

  print(f'Answer {round[0]}: {ans}')    

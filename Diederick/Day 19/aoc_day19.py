# %%

import re 

small = False

if small:
  with open('input19_small.txt') as f:
    data = f.read().split('\n')
else:
   with open('input19.txt') as f:
    data = f.read().split('\n')[:-1]

def dfs(bp,maxspend,cache,time,bots,amt):
  if time == 0:
    return amt[3]
  
  key = tuple([time,*bots,*amt])
  if key in cache:
    return cache[key]
  
  maxval = amt[3] + bots[3] * time
  
  for btype,recipe in enumerate(bp):
    if btype != 3 and bots[btype] >= maxspend[btype]:
      continue
    
    wait = 0
    
    for ramt, rtype in recipe:
      if bots[rtype] == 0:
        break
      wait = max(wait,-(-(ramt - amt[rtype] ) // bots[rtype]))
    else:
      remtime = time - wait - 1
      if remtime <= 0:
        continue
      bots_ = bots[:]
      amt_ = [x+y*(wait+1) for x,y in zip(amt,bots)]      
      
      for ramt,rtype in recipe:
        amt_[rtype] -= ramt
      bots_[btype] += 1
      for i in range(3):
        amt_[i] = min(amt_[i],maxspend[i]*remtime)
      maxval = max(maxval,dfs(bp,maxspend,cache,remtime,bots_,amt_))
  cache[key] = maxval
  return maxval
  
  
for idx,part in enumerate(["part1","part2"]):
  if part == "part1":
    total = 0
    data_part = data
  else:
    total = 1
    data_part = list(data)[:3]
  for i,line in enumerate(data_part):
    bp = []
    maxspend = [0, 0, 0]
    for section in line.split(": ")[1].split(". "):
      recipe = []
      for x,y in re.findall(r"(\d+) (\w+)",section):
        x = int(x)
        y = ["ore","clay","obsidian"].index(y)
        recipe.append((x,y))
        maxspend[y] = max(maxspend[y],x)
      bp.append(recipe)
    
    
    if part == "part1":
      v = dfs(bp,maxspend,{},24,[1,0,0,0],[0,0,0,0])
      total += (i+1)*v
    else: 
      v = dfs(bp,maxspend,{},32,[1,0,0,0],[0,0,0,0])
      total *= v
    
  print(f'Answer {idx+1}: {total}')


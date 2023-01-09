# Databricks notebook source
import re
import requests

day = 21
small = False

if small:
  with open('input21_small.txt') as f:
    data = f.read().splitlines()
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.splitlines()

data

# COMMAND ----------

monkey_known = {}
monkey_unknown = {}

for line in data:
  name = line.split(':')[0]
  if re.findall('[0-9]+', line) != []:
    monkey_known[name] = int(re.findall('[0-9]+', line)[0])
  else:
    monkey_unknown[name] = line.split(': ')[1]

print(monkey_known)
print(monkey_unknown)


# COMMAND ----------

pattern = r'\w+'

monkey_unknown1 = monkey_unknown.copy()
monkey_known1 = monkey_known.copy()

while monkey_unknown1:
  monkey_iter = monkey_unknown1.copy()
  for monkey in monkey_iter:
    monkeys = re.findall(pattern,monkey_iter[monkey])
    if monkeys[0] in monkey_known1.keys() and monkeys[1] in monkey_known1.keys():
      left = monkey_known1[monkeys[0]]
      right = monkey_known1[monkeys[1]]
      monkey_known1[monkey] = eval(monkey_iter[monkey].replace(monkeys[0],'left').replace(monkeys[1],'right'))
      del monkey_unknown1[monkey]
  
print(f"Answer 1: {int(monkey_known1['root'])}")

# COMMAND ----------


monkey_unknown2 = monkey_unknown.copy()

left = monkey_unknown2['root'][0:4]
left
right = monkey_unknown2['root'][7:11]
right


print(left,right)
print(monkey_unknown2)
print(monkey_known)


# COMMAND ----------

pattern = r'\w+'

i = 0
equal = False
while not equal:
  i +=1
  if i % 1000000 == 0:
    print(i)
  monkey_unknown2 = monkey_unknown.copy()
  monkey_known2 = monkey_known.copy()
  monkey_known2['humn'] = i
  while monkey_unknown2:
    monkey_iter = monkey_unknown2.copy()
    for monkey in monkey_iter:
      monkeys = re.findall(pattern,monkey_iter[monkey])
      if monkeys[0] in monkey_known2.keys() and monkeys[1] in monkey_known2.keys():
        left_i = monkey_known2[monkeys[0]]
        right_i = monkey_known2[monkeys[1]]
        monkey_known2[monkey] = eval(monkey_iter[monkey].replace(monkeys[0],'left_i').replace(monkeys[1],'right_i'))
        del monkey_unknown2[monkey]
  if monkey_known2[left] == monkey_known2[right]:
    equal = True

print(f"Answer 2: {i}")



# COMMAND ----------

i

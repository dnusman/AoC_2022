# Databricks notebook source
import requests

day = 25

small = False

if small:
  with open('input25_small.txt') as f:
    data = f.read().splitlines()
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.splitlines()
  
df = [[x for x in row] for row in data]

for row,line in enumerate(df):
  for col,char in enumerate(line):
    if char == '-':
      df[row][col] = '-1'
    elif char == '=':
      df[row][col] = '-2'

# COMMAND ----------

def snafu2int(loc,int):
  return int*(5**loc)

# COMMAND ----------

def int2snafu(int):
  res = []
  while int > 0:
    res.append("012=-"[int %5])
    int = (2+int) // 5
  return ''.join(res[::-1])

# COMMAND ----------

ans_1 = 0

for row,line in enumerate(df):
  sum = 0
  line = reversed(line)
  for col,character in enumerate(line):
    sum += snafu2int(col,int(character))

  ans_1 += sum
 
print(f'Answer 1: "{int2snafu(ans_1)}"')
    

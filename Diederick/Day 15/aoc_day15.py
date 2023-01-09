# Databricks notebook source
import pandas as pd
import datetime
import requests
import re

day = 15

small = False

if small:
  with open('input15_small.txt') as f:
    data = f.read().splitlines()
  Y = 10
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = r.text.splitlines()
  Y = 2000000

# COMMAND ----------

df = [[int(x) for x in re.findall(r'-?\d+', i)]  for i in data]

sensors = []
beacons = []
hashtags = set()

for i in range(len(df)):
  
  sensors.append((df[i][0],df[i][1]))
  beacons.append((df[i][2],df[i][3]))  



    

# COMMAND ----------

def manhatten_distance(point1,point2,Y):
  return abs(point1[0]-point2) + abs(point1[1]-Y)

def return_coordinates(sensor,dist,answer_row):
  coords = []
  for x in range(-dist,dist+1):
    if manhatten_distance(sensor,(sensor[0]+x),answer_row) <= dist:
      coords.append((sensor[0] + x, answer_row))    
  return coords


# COMMAND ----------

for i in range(len(df)):  
  sensor = sensors[i]
  beacon = beacons[i]
  dist = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
  
  for coord in return_coordinates(sensor,dist,Y):
    hashtags.add(coord)
    
print(f'Answer 1: {len(hashtags-set(beacons))}')

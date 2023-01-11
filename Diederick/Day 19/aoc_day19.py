# Databricks notebook source
import re 

with open('input19_small.txt') as f:
  data = f.read().split('\n\n')

blueprints = {}
  
for line in data:
  numbers = re.findall(r'\d+', line)
  blueprint = int(numbers[0])
  blueprints[blueprint] = list(map(int,numbers[1:]))

  



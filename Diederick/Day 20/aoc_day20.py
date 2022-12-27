# Databricks notebook source
with open('input20_small.txt') as f:
  data = f.read().splitlines()

original = []
for i,v in enumerate(data):
  original.append([int(v),i])

original

# COMMAND ----------

altered = original.copy()

for i,v in enumerate(original):
#   print(i)
  
  indices =list(range(len(original)))
  indices.remove(i)
  
  altered[i][1] += altered[i][0]
  
  for other in indices:
    if altered[i][0] > 0:
      altered[other][1] -= 1
    elif altered[i][0] <0:
      altered[other][1] += 1

print(altered)
  
  

  


# COMMAND ----------

altered = original.copy()

for i,v




# COMMAND ----------

def update_position(current_position,increment,length):
  if increment < 0:
    new_position = current_position + increment
    if new_position < 0:
      new_position = length-abs(new_position)
  else:
    new_position = current_position + increment
    if new_position > length:
      new_position = new_position - length
  return new_position


update_position(0,-1,7)

# COMMAND ----------

#rules

#1. new pos = 0:
# list = list + key

#2. new pos <0:
  
#   left = length - value under zero
#   right = list[-value under zero:]
#   left + key + right
#3. new pos > length:


for i in original:
  

# COMMAND ----------

for i in range(6,2,-1):
  print(i)

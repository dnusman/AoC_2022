# Databricks notebook source
from collections import deque
import requests 

small = False
day = 20

if small:
  with open("input20_small.txt") as f:
    data = [int(x) for x in f.read().splitlines()]
else:
  cookies = {'session': '53616c7465645f5f1f7b2f796a4556ee8ae4c0b6a01f75fb54e82194d3f8815048534e4e315ca6c5ee07402b983e327fc6b79a28b237c72ed1ea6f6157e38e1d'}
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

# COMMAND ----------

# toggle_example = True
# path_input = f'../input/day_{__file__.split(".")[0].split("_")[-1]}{"_example" if toggle_example else ""}.txt'


small = True
day = 20

if small:
  with open("input20_small.txt") as f:
    data = [int(x) for x in f.read().splitlines()]
else:
  cookies = {'session': '53616c7465645f5f0e0be1a0761339e0465a495ff5069c3d6a10a11c0caac7cbc6403ee58544f377cea286763e468e79b8742f07a024cd201ef42047fbe56d2d'}
  r = requests.get('https://adventofcode.com/2022/day/{0}/input'.format(day), cookies=cookies)
  data = [int(x) for x in r.text.splitlines()]



# with open(path_input, 'r') as input_file:
#     input = input_file.read().splitlines()

# encrypted_file = list(map(int, input))
encrypted_file = data
length = len(encrypted_file)
mixed_file = encrypted_file.copy()
index = list(range(length))
# print(mixed_file)


def mix_it_up(mixed_file, index):
    global length

    for i in range(length):
        current_position = index.index(i)
        moved_digit = mixed_file.pop(current_position)
        moved_index = index.pop(current_position)
        new_position = current_position + moved_digit

        while abs(new_position) > length:
            new_position = (new_position % length) + (new_position // length)

        mixed_file = mixed_file[: new_position] + [moved_digit] + mixed_file[new_position:]
        index = index[: new_position] + [moved_index] + index[new_position:]

    return mixed_file, index


for i in range(1):
    mixed_file, _ = mix_it_up(mixed_file, index)
    print(mixed_file)

index_zero = mixed_file.index(0)
answer_part_1 = 0
for j in [1000, 2000, 3000]:
    answer_part_1 += mixed_file[(j % length) + index_zero - length]
  
print(f'Answer 1: {answer_part_1}')

########################################################################################################################
decryption_key = 811589153
mixed_file = [x * decryption_key for x in encrypted_file]
index = list(range(length))
print(mixed_file, index)

for j in range(10):
    mixed_file, index = mix_it_up(mixed_file, index)
    print(mixed_file, index)
#
# index_zero = mixed_file.index(0)
# answer_part_2 = 0
# for j in [1000, 2000, 3000]:
#     answer_part_2 += mixed_file[(j % length) + index_zero - length]



# OLD
# if new_position == 0:
#     new_position = length
# elif new_position > length:
#     # while new_position > length:
#     #     new_position = new_position - length + 1
#     new_position = (new_position % length) + (new_position // length)
# elif new_position < 0:
#     # while new_position < 0:
#     #     new_position = length + new_position - 1
#     new_position = (new_position % length) + (new_position // length)

# COMMAND ----------

answer_part_1

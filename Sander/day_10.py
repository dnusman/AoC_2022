import numpy as np
from matplotlib import pyplot

toggle_example = False
path_input = f'../input/day_{__file__.split(".")[0].split("_")[-1]}{"_example" if toggle_example else ""}.txt'

with open(path_input, 'r') as input_file:
    input = input_file.read().splitlines()

add_list = []
cycles = [0]
for instruction in input:
    if instruction == 'noop':
        cycles += [cycles[-1] + 1]
        add_list += [0]
    else:
        V = int(instruction.split(' ')[1])
        cycles += [cycles[-1] + 1, cycles[-1] + 2]
        add_list += [0, V]

cycles = cycles[1:]
X = [1]
s = 1
for item in add_list:
    s += item
    X += [s]

interesting_cycles = [20, 60, 100, 140, 180, 220]
sums = []
for ic in interesting_cycles:
    sums += [X[ic - 1] * ic]

total_sum = sum(sums)

###############################################################
screen_width = 40
screen = np.zeros((int(len(X) / screen_width), screen_width))

i = 0
j = 0
for sp in X:
    if i in [sp - 1, sp, sp + 1]:
        screen[j, i] = 1
    if i == screen_width - 1:
        i = 0
        j += 1
        continue
    i += 1

pyplot.figure()
pyplot.imshow(screen)
pyplot.show()

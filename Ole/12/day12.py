import numpy as np
import pdb
with open("input") as f:
    heights = [list(x) for x in f.read().splitlines()]

start_y = [y for y in range(len(heights)) if 'S' in heights[y]][0]
start_x = heights[start_y].index('S')
end_y = [y for y in range(len(heights)) if 'E' in heights[y]][0]
end_x = heights[end_y].index('E')
heights[start_y][start_x] = "a"
heights[end_y][end_x] = "z"

heights = [list(map(lambda x: ord(x)-96, x)) for x in heights]
Y = len(heights)
X = len(heights[0])

fastest = [[X*Y]*X for _ in range(Y)]
fastest[start_y][start_x] = 0

# comment for pt1, uncomment for pt2
for x in range(X):
    for y in range(Y):
        if heights[y][x] == 1:
            fastest[y][x] = 0
# end pt2 mod

paths_updated = 1 # set to 1 to enter loop
loop_stop = 0

while loop_stop < 10:
    
    paths_updated = 0
    
    # loop over cells
    for x in range(X):
        for y in range(Y):
               
            # find the adjecent cells that are accessible
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_y = y + d[0]
                new_x = x + d[1]
                
                # check if valid step
                if new_y < 0 or new_y >= Y or new_x < 0 or new_x >= X or \
                    heights[new_y][new_x] > heights[y][x]+1:
                    continue
                
                # update path length with current tile + 1
                if fastest[new_y][new_x] > fastest[y][x]+1:
                    fastest[new_y][new_x] = fastest[y][x]+1
                    paths_updated += 1
    
    #print(f"current solution is {fastest[end_y][end_x]}")
            
    if paths_updated == 0:
        loop_stop += 1
    else:
        loop_stop = 0

print(fastest[end_y][end_x])
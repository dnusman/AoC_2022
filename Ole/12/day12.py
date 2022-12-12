import numpy as np
import pdb
with open("input-test") as f:
    heights = np.array([list(x) for x in f.read().splitlines()])

startpos = np.where(heights == "S")
startpos = [startpos[0][0], startpos[1][0]]
heights[startpos[0], startpos[1]] = "a"
endpos = np.where(heights == "E")
endpos = [endpos[0][0], endpos[1][0]]
heights[endpos[0], endpos[1]] = "z"


heights = np.array([list(map(lambda x: ord(x)-96, x)) for x in heights])
print(heights)

paths = [[startpos]]
for path_idx, path in enumerate(paths):
    # remove the path from path lists
    current_tile = path[-1]
    paths_created = 0

    # find the adjecent cells that are accessible
    for direction in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        print(f"at {current_tile}, going {direction}")
        new_tile = [current_tile[0] - direction[0],
                    current_tile[1] - direction[1]]
        if (np.array(new_tile) >= 0).all() and \
                new_tile[0] <= heights.shape[0] and \
                new_tile[1] <= heights.shape[1] and \
                heights[new_tile[0], new_tile[1]] <= \
                heights[current_tile[0], current_tile[1]]+1 and \
                new_tile != endpos and \
                new_tile not in path:
            newpath = path + [new_tile]
            print(f"appending {newpath}")
            paths.append(newpath)
            paths_created += 1

    paths.pop(path_idx)
    if paths_created == 0:
        break

print(min([len(x) for x in paths]))

import numpy as np
import pdb
with open("input") as f:
    scans = f.read().splitlines()

rocks = set()
sand_rest = set()
sand_flow = []
mapje = np.zeros((180, 60))
abyss = 0

for scan in scans:
    points = [list(map(int, x.split(','))) for x in scan.split(" -> ")]
    for i in range(0, len(points)-1):
        # loop over points and take the next one
        for x in range(min(points[i][0], points[i+1][0]),
                       max(points[i][0], points[i+1][0])+1):
            for y in range(min(points[i][1], points[i+1][1]),
                           max(points[i][1], points[i+1][1])+1):
                rocks.add((x, y))
                abyss = max(y, abyss)
                # mapje[y, x-465] = 1

for x in range(0, 1000):
    rocks.add((x, abyss+2))

# plt.imshow(mapje)
# plt.ion()
# plt.show(block=False)
solved_pt_1 = 0

for ts in range(150000):
    if ts % 5000 == 0:
        print(f"At ts {ts}")

    # add sand
    sand_flow.append((500, 0))

    # move all sand_flow
    for idx, grain_pos in enumerate(sand_flow):
        for next_pos in [(grain_pos[0], grain_pos[1]+1),     # first down
                         (grain_pos[0]-1, grain_pos[1]+1),   # then diag left
                         (grain_pos[0]+1, grain_pos[1]+1)]:  # then diag right
            if next_pos not in rocks and next_pos not in sand_rest:
                # move sand grain to new position
                sand_flow[idx] = next_pos
                if next_pos[1] > abyss and not solved_pt_1:
                    solved_pt_1 = 1
                    print(f"Answer part 1 is {len(sand_rest)}")

                break

        if sand_flow[idx] == grain_pos:

            # sand cannot move -- make it stationary
            sand_rest.add((grain_pos))
            sand_flow.pop(idx)

        if len(sand_flow) == 1 and ts > 1:
            print(f"Answer part 2 is {len((sand_rest))}")
            exit(0)

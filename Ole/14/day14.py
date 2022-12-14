import numpy as np
import matplotlib.pyplot as plt
with open("input") as f:
    scans = f.read().splitlines()

rocks = set()
sand_rest = []
sand_flow = []
mapje = np.zeros((180, 60))

for scan in scans:
    points = [list(map(int, x.split(','))) for x in scan.split(" -> ")]
    for i in range(0, len(points)-1):
        for x in range(min(points[i][0], points[i+1][0]),
                       max(points[i][0], points[i+1][0])+1):
            for y in range(min(points[i][1], points[i+1][1]),
                        max(points[i][1], points[i+1][1])+1):
                rocks.add((x, y))
                mapje[y, x-465] = 1

plt.imshow(mapje)
plt.ion()
plt.show(block=False)

for ts in range(10000):
    if ts % 500 == 0:
        print(f"At ts {ts}")
        plt.imshow(mapje)
        plt.show()
        plt.pause(0.0001)
        #print(sand_flow)
        #print(sand_rest)

    # add sand
    sand_flow.append((500, 0))
    new_sand_resting = 0

    # move all sand_flow
    for idx, grain_pos in enumerate(sand_flow):
        for next_pos in [(grain_pos[0], grain_pos[1]+1),     # first down
                         (grain_pos[0]-1, grain_pos[1]+1),   # then diag left
                         (grain_pos[0]+1, grain_pos[1]+1)]:  # then diag right
            if next_pos not in rocks and next_pos not in sand_rest:
                # move sand grain to new position
                sand_flow[idx] = next_pos
                break

        if sand_flow[idx] != next_pos:
            # sand cannot move -- make it stationary
            new_sand_resting = 1
            sand_rest.append(grain_pos)
            mapje[grain_pos[1], grain_pos[0]-465] = 2
            sand_flow.pop(idx)

    if not new_sand_resting and ts > 1000:
        break

print(f"Answer part 1 is {len(sand_rest)}")



with open("input10") as f:
    cmds = f.read().splitlines()

x = 1
answer = 0
strengths = range(0, 10000, 40)
img_y = 0
img_x = 0
img = ['' for _ in range(6)]

i = 0     # tracker for which command we are executing
executing = False
for c in range(1, 1000):

    if abs(x-img_x) <= 1:
        img[img_y] += "#"
    else:
        img[img_y] += "."

    if c % 40 == 0:
        img_y += 1
        img_x = -1
    img_x += 1

    if cmds[i] == "noop":
        i += 1

    else:
        if executing:
            x += int(cmds[i].split()[1])
            i += 1

        executing = not executing

    if i == len(cmds):
        break

for y in range(img_y):
    print(img[y])

print(c)

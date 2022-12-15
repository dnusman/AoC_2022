with open("input") as f:
    pairs = [list(map(eval, x.splitlines())) for x in f.read().split("\n\n")]


def comes_before(l, r):
    # returns 1 if left < right, 0 if right > left and None if right = left

    # print(f"\nChecking {l} v. {r}")

    # both ints --> compare
    if isinstance(l, int) and isinstance(r, int):
        if l != r:
            # print(f"Comparing ints {l} and {r}: {l > r}")
            return l < r
        # print(f"l[i] == r[i], continue")
        return None


    # one or more lists --> convert to lists and compare lists
    if isinstance(l, list) and isinstance(r, int):
        r = [r]
    if isinstance(r, list) and isinstance(l, int):
        l = [l]

    L = len(l)
    R = len(r)

    if R > 0 and L == 0:
        # print("Ran out of items left")
        return 1
    if L > 0 and R == 0:
        # print("Ran out of items right")
        return 0

    # find first item of outer list
    for i in range(max(L, R)):
        # print(i)
        if i >= L:
            # print("Ran out of items left")
            return 1
        if i >= R:
            # print("Ran out of items right")
            return 0

        comparison = comes_before(l[i], r[i])
        if comparison is None:
            continue
        return comparison

answer1 = 0

for idx, pair in enumerate(pairs):
    if comes_before(pair[0], pair[1]):
        # print(f"PAIR {idx+1} IS IN RIGHT ORDER")
        answer1 += idx+1
    else:
        pass
        # print(f"PAIR {idx+1} IS IN WRONG ORDER")

print(f"Answer part 1 is: {answer1}")


# binary sort - so compare with the middle one, then if smaller with the
# middle one of the smaller half etc. until nothing left/right, then insert
# there

packets = [[[2]], [[6]]] # include the divider packets
for pair in pairs:
    packets.extend(pair)

order = [] # start order w/ first packet


for i, packet in enumerate(packets):

    left = 0
    right = len(order)

    for _ in range(10):
        if left == right:
            break
        # print(f"L: {left}, R: {right}")

        # update left & right by comparing & splitting
        insert_i = left + ((right - left) // 2)

        if comes_before(packet, packets[order[insert_i]]):
            # print(f"{packet} comes before {packets[order[insert_i]]}")
            right = insert_i
        else:
            # print(f"{packet} comes after {packets[order[insert_i]]}")
            left = insert_i+1

    # insert into order
    order = order[:left] + [i] + order[right:]

    # print(f"Order now is {order}")

# print packets to check test output
# for o in order:
    # print(packets[o])

# the divider packets are packet 0 & 1, so finding their index in the order
# will give the answer

print(f"Answer to part 2 is {(order.index(0)+1) * (order.index(1)+1)}")

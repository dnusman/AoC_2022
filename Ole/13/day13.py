with open("input") as f:
    pairs = [list(map(eval, x.splitlines())) for x in f.read().split("\n\n")]


def right_order(l, r):
    # returns 1 if left > right, 0 if right < left and None if right = left

    print(f"\nChecking {l} v. {r}")

    # both ints --> compare
    if isinstance(l, int) and isinstance(r, int):
        if l != r:
            print(f"Comparing ints {l} and {r}: {l > r}")
            return l < r
        print(f"l[i] == r[i], continue")
        return None


    # one or more lists --> convert to lists and compare lists
    if isinstance(l, list) and isinstance(r, int):
        r = [r]
    if isinstance(r, list) and isinstance(l, int):
        l = [l]

    L = len(l)
    R = len(r)

    if R > 0 and L == 0:
        print("Ran out of items left")
        return 1
    if L > 0 and R == 0:
        print("Ran out of items right")
        return 0

    # find first item of outer list
    for i in range(max(L, R)):
        print(i)
        if i >= L:
            print("Ran out of items left")
            return 1
        if i >= R:
            print("Ran out of items right")
            return 0

        comparison = right_order(l[i], r[i])
        if comparison is None:
            continue
        return comparison

answer1 = 0

for idx, pair in enumerate(pairs):
    if right_order(pair[0], pair[1]):
        print(f"PAIR {idx+1} IS IN RIGHT ORDER")
        answer1 += idx+1
    else:
        print(f"PAIR {idx+1} IS IN WRONG ORDER")

print(f"Answer part 1 is: {answer1}")

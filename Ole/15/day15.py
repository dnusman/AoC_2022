import re

with open("input") as f:
    sensors = [tuple(map(int, re.findall(r"-*\d+", x))) for
               x in f.read().splitlines()]

# store begin & end points of coverage in a dict with structure
# {row: [(begin_cover1, end_cover1), (begin_cover2, end_cover2), ..]}

coverage = {}

for (sx, sy, bx, by) in sensors:

    # calculate manhattan distance as abs difference in y + x
    d = abs(sy - by) + abs(sx - bx)
    print(f"Analyzing sensor {sx}, {sy} seeing beacon {bx}, {by} at dist {d}")

    for row in range(sy-d, sy+d+1):
        coverage_width = d - abs(sy-row)
        row_coverage = (sx - coverage_width, sx + coverage_width)
        # print(f"At row {row}, cw={coverage_width}, c = {row_coverage}")

        if row in coverage:
            coverage[row].append(row_coverage)
        else:
            coverage[row] = [row_coverage]

row_inspect = 2000000

cols_covered = set()
# loop over covered intervals in the row and add covered cols to set
# because I don't want to think too hard about double counting for now
# this will probably come to haunt me in part 2 though...
for s_coverage in coverage[row_inspect]:
    for col in range(s_coverage[0], s_coverage[1]):
        cols_covered.add(col)

print(f"Answer to part 1 is {len(cols_covered)}")

# this already gave memory issues but silver star. need to think of different
# approach to get gold

# idea - each time update the range in that row
# if the row is full, no longer inspect it

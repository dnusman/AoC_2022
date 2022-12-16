import re

with open("input-test") as f:
    sensors = [tuple(map(int, re.findall(r"-*\d+", x))) for
               x in f.read().splitlines()]

# store begin & end points of coverage in a dict with structure
# {row: [(begin_cover1, end_cover1), (begin_cover2, end_cover2), ..]}

partial_rows = {}
full_rows = []
search_min = 0
search_max = 20

for (sx, sy, bx, by) in sensors:

    # calculate manhattan distance as abs difference in y + x
    d = abs(sy - by) + abs(sx - bx)
    print(f"Analyzing sensor {sx}, {sy} seeing beacon {bx}, {by} at dist {d}")

    for row in [r for r in range(sy-d, sy+d+1) if r not in full_rows]:
        coverage_width = d - abs(sy-row)
        row_coverage = (sx - coverage_width, sx + coverage_width)
        # print(f"At row {row}, cw={coverage_width}, c = {row_coverage}")

        if row in partial_rows:
            # check if in already existing interval, if so update that interval
            in_other_interval = False
            for idx, interval in enumerate(partial_rows[row]):
                if interval[0] <= row_coverage[0]:
                    partial_rows[row][idx] = (interval[0],
                                              max(interval[1],
                                                  row_coverage[1]))
                    in_other_interval = True
                elif interval[1] >= row_coverage[1]:
                    partial_rows[row][idx] = (min(interval[0],
                                                  row_coverage[0]),
                                              interval[1])
                    in_other_interval = True

            if not in_other_interval:
                partial_rows[row].append(row_coverage)
        else:
            partial_rows[row] = [row_coverage]

        if len(partial_rows[row]) == 1 and \
                partial_rows[row][0][0] <= search_min and \
                partial_rows[row][0][1] >= search_max:
            # row is fully covered, no longer inspect it
            full_rows += [row]
            partial_rows.pop(row)

print(partial_rows)

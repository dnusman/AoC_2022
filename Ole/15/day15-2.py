import re

with open("input") as f:
    sensors = [tuple(map(int, re.findall(r"-*\d+", x))) for
               x in f.read().splitlines()]

search_min = 0
search_max = 4000000

def merge_intervals(intervals):
    # merges list of intervals
    # returns new list
    
    # compare each interval with the subsequent intervals in the list
    for interval1 in intervals[:-1]:
        for interval2 in intervals[intervals.index(interval1)+1:]:
            match_right = interval1[0] <= interval2[1]+1 and interval1[0] >= interval2[0]
            match_left = interval1[1] >= interval2[0]-1 and interval1[1] <= interval2[1]
            match_right2 = interval2[0] <= interval1[1]+1 and interval2[0] >= interval1[0]
            match_left2 = interval2[1] >= interval1[0]-1 and interval2[1] <= interval1[1]

            
            if match_right or match_left or match_left2 or match_right2:
                merged_interval = (min(interval1[0], interval2[0]), max(interval1[1], interval2[1]))
                intervals[intervals.index(interval2)] = merged_interval
                intervals.pop(intervals.index(interval1))
                
    return intervals

for row in range(search_min, search_max+1):
    if row % (search_max // 100) == 0:
        print(f"Analyzing rows, at {(row / search_max) * 100}%")
        
    sorted_sensors = sorted(sensors, key=lambda x: abs(x[1]-row))
    row_coverage = []
    row_covered = False
    for (sx, sy, bx, by) in sorted_sensors:
        d = abs(sy - by) + abs(sx - bx)
        coverage_width = d - abs(sy-row)
        new_interval = (sx - coverage_width, sx + coverage_width)
        row_coverage = merge_intervals(row_coverage + [new_interval])
        
        # check if row fully covered
        if len(row_coverage) == 1 and row_coverage[0][0] <= search_min and \
                                      row_coverage[0][1] >= search_max:
            row_covered = True
            break
    if not row_covered:
        break
  
print(f"Row where the beacon must be: {row, row_coverage}")
y = row
x = min([x[1] for x in row_coverage]) + 1 # smallest endpoint of 2 intervals

print(f"Answer is therefore {x*4000000+y}")  
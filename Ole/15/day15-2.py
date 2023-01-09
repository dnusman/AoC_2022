import re

with open("input") as f:
    sensors = [tuple(map(int, re.findall(r"-*\d+", x))) for
               x in f.read().splitlines()]

search_min = 0
search_max = 4000000

def merge_intervals(intervals):
    # merges list of intervals
    # returns new list
    # first had a unwieldy solution for this, stole this cleaner solution
    # from hyperneutrino
    
    # sort such that all lows are descending 
    # (if the same low, sort will automatically look at the high)
    intervals.sort() 
    
    # initiate list of merged intervals
    merged = []
    
    for lo, hi in intervals:
        if not merged:
            merged.append([lo, hi])
            continue
        
        qhi = merged[-1][1]
        
        if lo > qhi+1:
            merged.append([lo, hi])
            continue
        
        merged[-1][1] = max(hi, qhi)
            
    return merged

for row in range(search_min, search_max+1):
    # output status (takes 1-2secs per %p on my machine)
    if row % (search_max // 10) == 0:
        print(f"Analyzing rows, at {(row / search_max) * 100:.0f}%")
        
    # sort sensors based on proximity to the row -- check most likely candidates to fully fill the row first
    sorted_sensors = sorted(sensors, key=lambda x: abs(x[1]-row))
    
    # initiate coverage trackers for this row
    row_coverage = []
    row_covered = False
    
    # loop over sensors
    for (sx, sy, bx, by) in sorted_sensors:
        
        # calculate "Manhattan radius" of sensor & coverage width in this row
        d = abs(sy - by) + abs(sx - bx)
        coverage_width = d - abs(sy-row)
        
        # if out of range, don't look at this sensor
        if coverage_width < 0:
            continue
                
        # calculate interval of coverage in this row
        new_interval = (sx - coverage_width, sx + coverage_width)
        row_coverage.append(new_interval)
    
    row_coverage = merge_intervals(row_coverage)
     
    # check if row fully covered, if so, no need to look at other sensors and on to the next row
    if len(row_coverage) == 1 and row_coverage[0][0] <= search_min and \
                                    row_coverage[0][1] >= search_max:
        row_covered = True
    
    # if loop completed without fully covering row, there must be a distress beacon!
    if not row_covered:
        break
  
print(f"Row where the beacon must be: {row, row_coverage}")
y = row
x = min([x[1] for x in row_coverage]) + 1 # smallest endpoint of 2 intervals

print(f"Answer is therefore {x*4000000+y}")  
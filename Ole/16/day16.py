import re
from collections import deque

caves = {}
flow_rates = {}
pattern = re.compile("(\d+|[A-Z]{2})")
with open("input") as f:
    lines = [pattern.findall(x) for x in f.read().splitlines()]
    
for line in lines:
    caves[line[0]] = line[2:]
    flow_rates[line[0]] = int(line[1])
    

def distance(graph, start, end):
    # breadth first search, stole from hyperneutrino earlier day
    if start == end:
        return 0
    
    visited = {(start)}
    q = deque()
    q.append((0, start))
    
    while q:
        d, n = q.popleft()
        for neighbour in graph[n]:
            if neighbour in visited:
                continue
            if neighbour == end:
                return d + 1
            visited.add(neighbour)
            q.append((d+1, neighbour))
        
        
distances = {}
for cave1 in caves:
    for cave2 in caves:
        distances[(cave1, cave2)] = distance(caves, cave1, cave2)
        
q = deque()
q.append((0, 0, ['AA']))
routes = []

# just list all combinations of opening the valves,
# taking into account the amount of time it will take
valves = [cave for cave in caves if flow_rates[cave] > 0]

while q:
    time, pressure_released, route = q.popleft()
    
    # loop over unvisited valves
    unvisited_valves = [valve for valve in valves if valve not in route]
    if not unvisited_valves:
        routes.append((pressure_released, route))
        continue
    
    for next_cave in unvisited_valves:
        dtime = distances[route[-1], next_cave] + 1
        if time + dtime > 30:
            routes.append((pressure_released, route))
            continue
        dpressure_released = (30 - time - dtime) * flow_rates[next_cave]
        q.append((time+dtime, pressure_released + dpressure_released, route + [next_cave]))
        
    if len(q) % 10000 == 0:
        print(f"q is now {len(q)}")
        
        
print(max([x[0] for x in routes]))


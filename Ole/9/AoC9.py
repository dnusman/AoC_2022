with open("input9.txt") as f:
    moves = [x.split(' ') for x in f.read().splitlines()]

# start all at 0,0
hpos = [0, 0]
tpos = [0, 0]
tposs = set()

for direction, count in moves:
    for _ in range(int(count)):
        
        # move head
        if direction == "R":
            hpos[0] += 1
        if direction == "L":
            hpos[0] -= 1  
        if direction == "U":
            hpos[1] += 1
        if direction == "D":
            hpos[1] -= 1     
            
        # calculate delta w/ tail
        dx = hpos[0] - tpos[0]
        dy = hpos[1] - tpos[1]
        
        if abs(dx) == 2 or abs(dy) == 2:
            tpos[0] += min(1, max(-1, dx))   
            tpos[1] += min(1, max(-1, dy))   
            
        tposs.add(tuple(tpos))

    
print(f"Part 1: {len(tposs)}")
        
## Part 2

# start all at 0,0
snake = [[0,0] for _ in range(10)]
tposs = set()

for direction, count in moves:
    for _ in range(int(count)):
        
        # move head
        if direction == "R":
            snake[0][0] = snake[0][0] + 1
        if direction == "L":
            snake[0][0] -= 1  
        if direction == "U":
            snake[0][1] += 1
        if direction == "D":
            snake[0][1] -= 1     
            
        # loop over rest of snake to move the bodyparts
        
        for i in range(1,10):
            # calculate delta w/ previous part
            dx = snake[i-1][0] - snake[i][0]
            dy = snake[i-1][1] - snake[i][1]
        
            if abs(dx) == 2 or abs(dy) == 2:
                snake[i][0] += min(1, max(-1, dx))   
                snake[i][1] += min(1, max(-1, dy))   
            
        tposs.add(tuple(snake[9]))
        
print(f"Part 2: {len(tposs)}")
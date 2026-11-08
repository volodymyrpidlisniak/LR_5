import math

x, y = 0, 0

while True:
    line = input()
    if not line:
        break
    
    direction, steps = line.split()
    steps = int(steps)
    
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = round(math.sqrt(x**2 + y**2))

print(distance)
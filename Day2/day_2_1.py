import math

def change_position(horizontal, depth, direction, value):
    if direction == 'forward':
        horizontal += value
    elif direction == 'down':
        depth += value
    elif direction == 'up':
        depth -= value
    return horizontal, depth



f = open('/Users/Jochem/Documents/Coding/AdventOfCode21/Day2/puzzle_input.txt', 'r')
lines = f.readlines()

horizontal = 0
depth = 0
for line in lines:
    direction, value = line.split(' ')
    value = int(value)
    horizontal, depth = change_position(horizontal, depth, direction, value)

print(horizontal*depth)

import math

def change_position(horizontal, depth, aim, direction, value):
    if direction == 'forward':
        horizontal += value
        depth += aim*value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    return horizontal, depth, aim



f = open('/Users/Jochem/Documents/Coding/AdventOfCode21/Day2/puzzle_input.txt', 'r')
lines = f.readlines()

horizontal = 0
depth = 0
aim = 0
for line in lines:
    direction, value = line.split(' ')
    value = int(value)
    horizontal, depth, aim = change_position(horizontal, depth, aim, direction, value)

print(horizontal*depth)

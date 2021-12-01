import math

with open('/Users/Jochem/Documents/Coding/AdventOfCode21/Day1/input_text.txt') as f:
    lines = f.readlines()

increases = 0
for i in zip(lines[:-1], lines[1:]):
    if int(i[1])-int(i[0]) > 0:
        increases += 1

print(increases)
    
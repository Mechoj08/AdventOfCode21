import math

with open('/Users/Jochem/Documents/Coding/AdventOfCode21/Day1/input_text.txt') as f:
    lines = f.readlines()

a = lines[:-2]
b = lines[1:-1]
c = lines[2:]

sums = []
for i in zip(a, b, c):
    sums.append(int(i[0]) + int(i[1]) + int(i[2]))

increases = 0
for i in zip(sums[:-1], sums[1:]):
    if i[1]-i[0] > 0:
        increases += 1

print(sums)
print(increases)
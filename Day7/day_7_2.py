import math

def parse_input():
    positions =  [int(i) for i in open('Day7/puzzle_input.txt').readline().split(',')]
    return positions

def alignment(positions):
    total_fuel = ((max(positions)+1)**2)*len(positions)
    align = - 1
    for i in range(max(positions)+1):
        fuel = sum([int((abs(i - change))*(abs(i-change)+1)/2) for change in positions])
        if fuel < total_fuel:
            align = i
            total_fuel = fuel
    return (align, total_fuel)

print(alignment(parse_input()))
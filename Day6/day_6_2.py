import math

def parse_input():
    rates = open('Day6/puzzle_input.txt').readline()
    population = [int(rate) for rate in rates.split(',')]
    counts = [0]*9
    for i in population:
        counts[i] += 1
    return counts

def reproduce_day(counts):
    new_counts = [0]*9
    for i, val in enumerate(counts[:-1]):
        new_counts[i] += counts[i+1]
    new_counts[6] += counts[0]
    new_counts[8] += counts[0]
    return new_counts

def reproduce(days, start):
    day = 1
    fish_track = start
    while day <= days:
        new_fish = reproduce_day(fish_track)
        fish_track = new_fish
        day += 1
        print(sum(fish_track))
    return sum(fish_track)

print(reproduce(256, parse_input()))
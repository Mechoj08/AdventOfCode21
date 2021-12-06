import math

def parse_input():
    rates = open('Day6/puzzle_input.txt').readline()
    #First index of tuple is fish label, second is the age
    population = [int(rate) for rate in rates.split(',')]
    return population

def reproduce_gen(fish_list):
    next_gen = []
    for fish in fish_list:
        if fish != 0:
            next_gen.append(fish-1)
        else:
            next_gen.extend([6, 8])
    return next_gen

def reproduce(days, start):
    day = 1
    fish_track = start
    while day <= days:
        new_fish = reproduce_gen(fish_track)
        fish_track = new_fish
        day += 1
        print(day)
    return len(new_fish)

print(reproduce(256, parse_input()))

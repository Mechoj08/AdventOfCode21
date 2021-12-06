import math

def parse_input():
    rates = open('Day6/puzzle_input.txt').readline()
    #First index of tuple is fish label, second is the age
    population = {}
    for i, rate in enumerate(rates.split(',')):
        population[i] = int(rate)
    return population

def reproduce_gen(fish_dict):
    new_fish_dict = {}
    for fish in fish_dict:
        if fish_dict[fish] == 0:
            fish_dict[fish] = 6
            new_fish_dict[fish] = 8
        else:
            fish_dict[fish] -= 1
    for i, new_fish in enumerate(new_fish_dict):
        fish_dict[len(fish_dict)+i] = 8
    return fish_dict

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
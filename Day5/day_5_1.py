import math

def parse_input():
    coordinate_pairs = []
    for line in open('Day5/puzzle_input.txt').readlines():
        start, end = line.split(' -> ')
        start_x, start_y = start.split(',')
        start = complex(int(start_x), int(start_y))
        end_x, end_y = end.split(',')
        end = complex(int(end_x), int(end_y))
        coordinate_pairs.append([start, end])
    return coordinate_pairs

def horizontal_vertical(coordinate_pairs):
    new_pairs = []
    for i in coordinate_pairs:
        if (i[1]-i[0]).real == 0 or (i[1]-i[0]).imag == 0:
            new_pairs.append(i)
    return new_pairs
    
def covered_coordinates(pair):
    #This is an implementation for horizontal and vertical lines
    start = pair[0]
    end = pair[1]
    covered = []
    diff = end-start
    if diff.real == 0:
        if diff.imag > 0:
            for i in range(int(abs(diff.imag))+1):
                covered.append(start+complex(0, i))
        else:
            for i in range(int(abs(diff.imag))+1):
                covered.append(end+complex(0, i))
    else:
        if diff.real > 0:
            for i in range(int(abs(diff.real))+1):
                covered.append(start+complex(i, 0))
        else:
            for i in range(int(abs(diff.real))+1):
                covered.append(end+complex(i, 0))
    return covered


def add_coordinates(listed_coordinates, new_coordinates):
    #listed_coordinates is a dictionary with counts of current coordinates
    #coordinates are a number of coordinates that we want to add to listed
    for coords in new_coordinates:
        if coords in listed_coordinates:
            listed_coordinates[coords] += 1
        else:
            listed_coordinates[coords] = 1
    return listed_coordinates

def count_common_coordinates(listed_coordinates):
    common_counts = 0
    for key in listed_coordinates:
        if listed_coordinates[key] > 1:
            common_counts += 1
    return common_counts

def puzzle_1():
    original_pairs = parse_input()
    left_over_pairs = horizontal_vertical(original_pairs)
    all_coordinates = []
    for pair in left_over_pairs:
        all_coordinates.append(covered_coordinates(pair))
    dictionary_counts = {}
    for lines in all_coordinates:
        dictionary_counts = add_coordinates(dictionary_counts, lines)
    return dictionary_counts

    
print(count_common_coordinates(puzzle_1()))

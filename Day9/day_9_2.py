import math
import numpy as np

def parse_input():
    matrix = []
    f = open('Day9/puzzle_input.txt', 'r')
    first_line = f.readline()
    matrix.append([9]*(len(first_line)+1))
    templ = [9]
    templ.extend([int(i) for i in first_line[:-1]])
    templ.extend([9])
    matrix.append(templ)
    for line in f.readlines():
        templ = [9]
        templ.extend([int(i) for i in line[:-1]])
        templ.extend([9])
        matrix.append(templ)
    matrix.append([9]*(len(first_line)+1))
    return np.array(matrix)


def compare_elements(matrix):
    low_points = []
    x_shape, y_shape = matrix.shape
    for row in range(1, x_shape-1):
        for column in range(1, y_shape-1):
            up = matrix[row-1][column]
            down = matrix[row+1][column]
            left = matrix[row][column-1]
            right = matrix[row][column+1]
            current_point = matrix[row][column]
            if current_point < up and current_point < down and current_point < left and current_point < right:
                low_points.append((current_point, row, column))
    return low_points

#Create list of unactive nodes, neutral nodes and active nodes. Start from lowest point and inspect neighbours. All neighbours that are higher, but not 9 are added to queue of active nodes. Deactivate current node and put it in unactive nodes. Then repeat for nodes that are left in the active queue.

def find_basin(matrix, low_point):
    seen = set([low_point])
    active = set([low_point])
    while active:
        next_active = set()
        for item in active:
            y_c = item[1]
            x_c = item[2]
            #up-check
            if matrix[y_c-1][x_c] != 9 and matrix[y_c-1][x_c] > item[0] and (matrix[y_c-1][x_c], y_c-1, x_c) not in seen:
                seen.add((matrix[y_c-1][x_c], y_c-1, x_c))
                next_active.add((matrix[y_c-1][x_c], y_c-1, x_c))
            #down-check
            if matrix[y_c+1][x_c] != 9 and matrix[y_c+1][x_c] > item[0] and (matrix[y_c+1][x_c], y_c+1, x_c) not in seen:
                seen.add((matrix[y_c+1][x_c], y_c+1, x_c))
                next_active.add((matrix[y_c+1][x_c], y_c+1, x_c))
            #left-check
            if matrix[y_c][x_c-1] != 9 and matrix[y_c][x_c-1] > item[0] and (matrix[y_c][x_c-1], y_c, x_c-1) not in seen:
                seen.add((matrix[y_c][x_c-1], y_c, x_c-1))
                next_active.add((matrix[y_c][x_c-1], y_c, x_c-1))
            #right-check
            if matrix[y_c][x_c+1] !=9 and matrix[y_c][x_c+1] > item[0] and (matrix[y_c][x_c+1], y_c, x_c+1) not in seen:
                seen.add((matrix[y_c][x_c+1], y_c, x_c+1))
                next_active.add((matrix[y_c][x_c+1], y_c, x_c+1))
        active = next_active
    return seen

def count_basin(matrix, low_points):
    basins = []
    for low_point in low_points:
        basin = len(find_basin(matrix, low_point))
        basins.append(basin)
    basins.sort()
    return basins[-1]*basins[-2]*basins[-3]


print(count_basin(parse_input(), compare_elements(parse_input())))
        

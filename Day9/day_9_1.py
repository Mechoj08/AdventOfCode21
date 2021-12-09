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
                low_points.append(current_point)
    return low_points

low_points_output = compare_elements(parse_input())
total = 0
for i in low_points_output:
    total += i + 1
print(total)

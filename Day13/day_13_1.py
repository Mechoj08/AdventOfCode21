import math
import numpy as np

def parse_input():
    dots, folds = open('Day13/puzzle_input.txt', 'r').read().split('\n\n')
    dots = set(tuple(int(i) for i in line.split(',')) for line in dots.split('\n'))
    folds = [tuple((line.split('=')[0][-1], int(line.split('=')[1]))) for line in folds.split('\n')]
    return dots, folds

def fold(dots, instruction):
    folded_dots = set()
    for dot in dots:
        if instruction[0] == 'x':
            if dot[0] > instruction[1]:
                new_dot = (2*instruction[1]-dot[0], dot[1])
                folded_dots.add(new_dot)
            else:
                folded_dots.add(dot)
        elif instruction[0] == 'y':
            if dot[1] > instruction[1]:
                new_dot = (dot[0], 2*instruction[1]-dot[1])
                folded_dots.add(new_dot)
            else:
                folded_dots.add(dot)
    return folded_dots

dots, instructions = parse_input()

def fold_all(dots, instructions):
    for inst in instructions:
        dots = fold(dots, inst)
    return dots

def paper_print(dots):
      for i in range(max([y for x, y in dots]) + 1):
            print(''.join('#' if (j, i) in dots else ' ' for j in range(max([x for x, y in dots]) + 1)))

print(paper_print(fold_all(dots, instructions)))


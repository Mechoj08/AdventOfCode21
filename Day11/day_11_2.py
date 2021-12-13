import math
import numpy as np

cap = lambda i: i if i>=0 else 11
def parse_input():
	input = []
	for line in open('Day11/test_input.txt').readlines():
		input.append([int(i) for i in line[:-1]])
	return np.array(input)

					
def neighbour_mask(x, y, grid, flashed):
	for i in range(-1, 2):
		for j in range(-1, 2):
			try:
				if flashed[x+i, y+j] == 0:
					grid[cap(x+i), cap(y+j)] += 1
			except: pass
	return grid


def update(grid):
	len_col, len_row = grid.shape
	grid = grid + 1
	flashed_tiles = np.zeros(grid.shape)
	while np.max(grid) > 9:
		for i in range(len_col):
			for j in range(len_row):
				if grid[i][j] > 9 and flashed_tiles[i][j] == 0:
					flashed_tiles[i][j] = 1
					grid = neighbour_mask(i, j, grid, flashed_tiles)
					grid[i, j] = 0
	return grid, np.sum(flashed_tiles)

def updates(steps, grid):
	total_flashes = 0
	step = 0
	len_col, len_row = grid.shape
	while total_flashes != 100:
		step +=1
		grid, flashed_total = update(grid)
		total_flashes = flashed_total
	return step

print(updates(100, parse_input()))
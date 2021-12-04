import math
import numpy as np
#Parse input

def read_bingo_board(current_board, new_line):
	bingo_add = [int(i) for i in new_line.split()]
	current_board.append(bingo_add)
	return current_board

with open('Day4/puzzle_input.txt', 'r') as f:
	random_numbers = f.readline()
	random_numbers = [int(i) for i in random_numbers.split(',')]
	f.readline()

	bingo_boards = []
	bingo_board = []
	rest = f.readlines()
	for line in rest:
		if line == '\n':
			bingo_board = np.array(bingo_board)
			bingo_boards.append((bingo_board, np.zeros(bingo_board.shape)))
			bingo_board = []
		else:
			bingo_board = read_bingo_board(bingo_board, line)

number_of_boards = len(bingo_boards)
win_check = [0]*number_of_boards

for RNG in random_numbers:
	for i, board in enumerate(bingo_boards):
		for location in np.argwhere(board[0] == RNG):
			board[1][location[0]][location[1]] = 1
		#Check if the board has completed vertical or horizontal rows
		row_check = np.matmul(board[1], np.ones(5))
		column_check = np.matmul(np.ones(5), board[1])
		if (5 in row_check) or (5 in column_check):
			unchecked_numbers = np.multiply(np.ones((5, 5)) - board[1], board[0])
			sum_unchecked = np.sum(unchecked_numbers)
			win_check[i] = 1
			if sum(win_check) == number_of_boards:
				print(sum_unchecked*RNG)




print(sum_unchecked)
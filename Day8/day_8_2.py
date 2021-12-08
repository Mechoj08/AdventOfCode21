import math

def parse_input():
	outputs = []
	cyphers = []
	for line in open('Day8/puzzle_input.txt').readlines():
		cypher, output = line.split(' | ')
		output = output[:-1].split(' ')
		outputs.append(output)
	return outputs

def digit_to_vector(digit):
    digit_vector = [0]*7
    possible_digits = 'abcdefg'
    for i in digit:
        digit_vector[possible_digits.index(i)] += 1
    return digit_vector

def vector_cypher(digit_vector):
    numbers = {'0': [1, 1, 1, 1, 1, 0, 1], 1: [1, 1, 0, 0, 0, 0, 0],
    '2': [1, 0, 1, 1, 0, 1, 1], '3': [1, 1, 1, 1, 0, 1, 0], '4': [1, 1, 0, 0, 1, 1, 0], '5': [0, 1, 1, 1, 1, 1, 0], '6': [0, 1, 1, 1, 1, 1, 1], '7': [1, 1, 0, 1, 0, 0, 0], '8': [1, 1, 1, 1, 1, 1, 1], '9': [1, 1, 1, 1, 1, 1, 0]}
    for key in numbers:
        if numbers[key] == digit_vector:
            return key

def give_back_displays(outputs):
    total = 0
    for line in outputs:
        display = ''
        for i in line:
            vector = digit_to_vector(i)
            vector_encoded = vector_cypher(vector)
            display += vector_encoded
        display = int(display)
        total += display
    return total

print(give_back_displays(parse_input()))
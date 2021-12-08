import math

def parse_input():
	outputs = []
	cyphers = []
	for line in open('Day8/puzzle_input.txt').readlines():
		cypher, output = line.split(' | ')
		output = output[:-1].split(' ')
		outputs.append(output)
	return outputs

def count_outputs(outputs):
	counter = 0
	for i in outputs:
		for j in i:
			if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
				counter += 1
	return counter

print(parse_input())
print(count_outputs(parse_input()))

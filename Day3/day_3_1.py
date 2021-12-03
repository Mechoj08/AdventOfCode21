import math


input_array = [line[:-1] for line in open('Day3/puzzle_input.txt').readlines()]
counts = [0]*len(input_array[0])
for bit_string in input_array:
    for i, bits in enumerate(bit_string):
        counts[i] += int(bits)

gamma_str = ''
for i in counts:
    if i >= len(input_array)/2:
        gamma_str += '1'
    else:
        gamma_str += '0'

epsilon_str = ''
for i in counts:
    if i < len(input_array)/2:
        epsilon_str += '1'
    else:
        epsilon_str += '0'

gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)

print(gamma*epsilon)




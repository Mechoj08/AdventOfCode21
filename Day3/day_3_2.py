import math
import copy

#Input data
input_array = [line[:-1] for line in open('Day3/puzzle_input.txt').readlines()]
oxygen_array = input_array
CO_array = copy.deepcopy(input_array)

def find_most_counts(counted_array):
    counts = [0]*len(counted_array[0])
    for bit_string in counted_array:
        for i, bits in enumerate(bit_string):
            counts[i] += int(bits)
    
    count_string = ''
    #print(counts)
    for i in counts:
        if i>= math.ceil(len(counted_array)/2):
            count_string += '1'
        else:
            count_string += '0'
    return count_string

def find_least_counts(counted_array):
    counts = [0]*len(counted_array[0])
    for bit_string in counted_array:
        for i, bits in enumerate(bit_string):
            counts[i] += int(bits)
    
    count_string = ''
    for i in counts:
        print(i)
        if i < int(math.ceil(len(counted_array)/2)):
            count_string += '1'
        else:
            count_string += '0'
    return count_string

#print(find_most_counts(oxygen_array))


#Select the oxygen string
for i, val in enumerate(find_most_counts(oxygen_array)):
    current_string = find_most_counts(oxygen_array)
    removals = []
    for j in oxygen_array:
        if current_string[i] != j[i]:
            removals.append(j)
    for x in removals:
        if len(oxygen_array) == 1:
            break
        oxygen_array.remove(x)

#Select the CO_2 string
for i, val in enumerate(find_least_counts(CO_array)):
    current_string = find_least_counts(CO_array)
    print(CO_array)
    print(current_string)
    removals = []
    for j in CO_array:
        if current_string[i] != j[i]:
            removals.append(j)
    for x in removals:
        if len(CO_array) == 1:
            break
        CO_array.remove(x)

print(oxygen_array)
print(CO_array)


print(int(oxygen_array[0], 2)*int(CO_array[0], 2))
import math

def parse_input():
	outputs = []
	cyphers = []
	for line in open('Day8/puzzle_input.txt').readlines():
		cypher = line.split(' | ')[0]
		output = line.split(' | ')[1]
		cyphers.append([set(i) for i in cypher.split(' ')])
		outputs.append([set(i) for i in output[:-1].split(' ')])
	return cyphers, outputs

def get_mapping(strings):
	all_words = set('abcdefg')
	mapping = {}
	#Map the easy letters
	for combination in strings:
		if len(combination) == 2:
			mapping[1] = combination
		elif len(combination) == 4:
			mapping[4] = combination
		elif len(combination) == 3:
			mapping[7] = combination
		elif len(combination) == 7:
			mapping[8] = combination
	len_five_words = []
	len_six_words = []
	for words in strings:
		if len(words) == 5:
			len_five_words.append(words)
		elif len(words) == 6:
			len_six_words.append(words)
	#Map number 2 to set
	for words in len_five_words:
		four_complement = all_words - mapping[4]
		if words & four_complement == four_complement:
			mapping[2] = words
	#Map number 6 to set
	for words in len_six_words:
		seven_complement = all_words - mapping[7]
		if words & seven_complement == seven_complement:
			mapping[6] = words
	#Map number 5 to set
	for words in len_five_words:
		two_complement = all_words-mapping[2]
		if words & two_complement == two_complement:
			mapping[5] = words
	#Map number 3 to set
	for words in len_five_words:
		if words not in mapping.values():
			mapping[3] = words
	for words in len_six_words:
		if words & mapping[3] == mapping[3]:
			mapping[9] = words
	for words in len_six_words:
		if words not in mapping.values():
			mapping[0] = words
	return mapping



def give_back_displays(cyphers, outputs):
	total = 0
	for i, cypher in enumerate(cyphers):
		mapping = get_mapping(cypher)
		display = ''
		for j in outputs[i]:
			for key in mapping:
				if mapping[key] == j:
					display = display + str(key)
		total += int(display)
	return total

o = parse_input()

print(give_back_displays(o[0], o[1]))

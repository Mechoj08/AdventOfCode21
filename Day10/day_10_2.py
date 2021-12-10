import math

def parse_input():
    input = []
    input = [line[:-1] for line in open('Day10/puzzle_input.txt', 'r').readlines()]
    return input

def check_line(line):
    starts = ['[', '(', '<', '{']
    closes = [']', ')', '>', '}']
    scores = {')':3 , ']':57 , '}':1197 , '>': 25137}
    queue = []

    for char in line:
        if char in starts:
            queue.append(char)
        else:
            if queue[-1] == starts[closes.index(char)]:
                queue.pop()
            else:
                expected = closes[starts.index(queue[-1])]
                #print('Expected ' + expected + ', got ' + char)
                return scores[char]
    return queue

def check_lines(lines):
    totals = []
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    for line in lines:
        total_line = 0
        output = check_line(line)
        if type(output) != int and output != []:
            for i in reversed(output):
                total_line = 5*total_line + scores[i]
            totals.append(total_line)
    totals.sort()
    return totals[int(len(totals)/2)]


print(check_lines(parse_input()))
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
    score = 0
    for line in lines:
        output = check_line(line)
        if type(output) == int:
            #print(output)
            score += output
    return score


print(check_lines(parse_input()))
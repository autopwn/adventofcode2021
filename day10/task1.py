#!/usr/bin/env python3
import sys

class AutoCompleteFinishedException(Exception):
    pass

class IncorrectLineException(Exception):
    pass

opens = ['(', '[', '{', '<']
closes = [')', ']', '}', '>']
val_illegal = {')': 3, ']': 57, '}': 1197, '>': 25137}

def check_line(line, open = ''):

    while line:
        if line[0] in opens:
            line = check_line(line[1:], line[0])
        elif line[0] in closes and closes.index(line[0]) == opens.index(open):
            return line[1:]
        else:
            raise IncorrectLineException(val_illegal[line[0]])

def autocomplete_line(line, idx = 0, open = ''):

    total_score = 0

    while idx < len(line):
        if line[idx] in opens:
            tmp_idx, total_score = autocomplete_line(line, idx + 1, line[idx])
            if tmp_idx >= 0:
                idx = tmp_idx
            else:
                if open:
                    return -1, total_score * 5 + (opens.index(open) + 1)
                else:
                    raise AutoCompleteFinishedException(total_score)
        elif line[idx] in closes and closes.index(line[idx]) == opens.index(open):
            return idx + 1, total_score
        else:
            raise Exception('Incorrect line should not happen in task 2')

    return -1, total_score * 5 + (opens.index(open) + 1)

def task1(data):

    remaining_lines = []
    sum = 0

    for line in data.split("\n"):
        try:
            check_line(line)
            remaining_lines.append(line)
        except IncorrectLineException as e:
            sum += int(str(e))

    print(f"task 1: {sum}")
    return remaining_lines

def task2(data):

    scores = []

    for line in data:
        try:
            autocomplete_line(line)
        except AutoCompleteFinishedException as e:
            scores.append(int(str(e)))

    middle_score = sorted(scores)[len(scores)//2]
    print(f"task 2: {middle_score}")

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        remaining_lines = task1(data)
        task2(remaining_lines)

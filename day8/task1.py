#!/usr/bin/env python3
from collections import Counter

def task1(data):

    c = Counter()
    for line in data.split('\n'):
        for digit in line.split(' | ')[1].split():
            c[len(digit)] += 1
    print(c[2] + c[3] + c[4] + c[7])

def task2(data):

    digits = {
        '012456': '0', '25': '1', '02346': '2', '02356': '3',
        '1235': '4', '01356': '5', '013456': '6', '025': '7',
        '0123456': '8', '012356': '9'
    }

    sum = 0

    for line in data.split('\n'):

        segments = [''] * 7

        input = line.split(' | ')[0].split()
        output = line.split(' | ')[1].split()

        one = [x for x in input if len(x) == 2][0]
        four = [x for x in input if len(x) == 4][0]
        seven = [x for x in input if len(x) == 3][0]
        eight = [x for x in input if len(x) == 7][0]

        segments[0] = [x for x in seven if x not in one][0]
        segments[5] = [y for y in [x for x in input if len(x) == 6 and (one[0] in x or one[1] in x) and not (one[0] in x and one[1] in x)][0] if one[0] in y or one[1] in y][0]
        segments[2] = [x for x in one if x != segments[5]][0]
        segments[3] = [y for y in four if y not in one and y in [x for x in input if len(x) == 5 and (one[0] in x and one[1] in x)][0]][0]
        segments[1] = [y for y in four if y not in one and y not in [x for x in input if len(x) == 5 and (one[0] in x and one[1] in x)][0]][0]
        segments[6] = [y for y in [x for x in input if len(x) == 5 and (one[0] in x and one[1] in x)][0] if y not in [segments[2], segments[5], segments[0], segments[3]]][0]
        segments[4] = [x for x in eight if x not in segments][0]

        sum += int(''.join([digits[''.join(sorted([str(segments.index(x)) for x in out]))] for out in output]))

    print(sum)

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        file_content = f.read().strip()
        #task1(file_content)
        task2(file_content)

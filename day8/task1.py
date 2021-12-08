#!/usr/bin/env python3
from collections import Counter

def task1(data):

    c = Counter()
    for line in data.split('\n'):
        for digit in line.split(' | ')[1].split():
            c[len(digit)] += 1
    print(c[2] + c[3] + c[4] + c[7])

def task2(data):

    # Manual mapping of sorted active display-segments to actual numbers
    # For example: number '1' has segments 2 and 5 active, thus '25' = '1'
    #
    #    0 
    # 1     2
    #    3
    # 4     5
    #    6
    digits = {
        '012456': '0', '25': '1', '02346': '2', '02356': '3',
        '1235': '4', '01356': '5', '013456': '6', '025': '7',
        '0123456': '8', '012356': '9'
    }

    sum = 0

    for line in data.split('\n'):

        segments = [''] * 7
        input, output = [x.split() for x in line.split(' | ')]

        # get signals with known length for number 1,4,7,8
        one = [x for x in input if len(x) == 2][0]
        four = [x for x in input if len(x) == 4][0]
        seven = [x for x in input if len(x) == 3][0]
        eight = [x for x in input if len(x) == 7][0]

        # get signal wire for top segment (0) by comparing numbers 1 and 7
        segments[0] = [x for x in seven if x not in one][0]
        # get signal wire for bottom right segment (5) by comparing 1 and 6
        segments[5] = [y for y in [x for x in input if len(x) == 6 and (one[0] in x or one[1] in x) and not (one[0] in x and one[1] in x)][0] if one[0] in y or one[1] in y][0]
        # get top right segment (2) by taking the one segment of 1 not part of 6
        segments[2] = [x for x in one if x != segments[5]][0]

        # numbers 2, 3 and 5 use five segments, but only number 3 intersects with segments of number 1, that's how we identify number 3
        # save in varable as we need it multiple times
        signal_for_three = [x for x in input if len(x) == 5 and (one[0] in x and one[1] in x)][0]

        # get middle segment (3) by comparing 1, 4 and 5
        segments[3] = [y for y in four if y not in one and y in signal_for_three][0]
        # get top left segment (1) by inversing the previous comparison
        segments[1] = [y for y in four if y not in one and y not in signal_for_three][0]
        # get bottom segment by removing all yet known segments from number 3
        segments[6] = [y for y in signal_for_three if y not in [segments[2], segments[5], segments[0], segments[3]]][0]
        # bottom left segment (4) is the only remaining segmet
        segments[4] = [x for x in eight if x not in segments][0]

        # now the list 'segments' contains one character for each segment of the display,
        # so we just do a lookup in the hand-made mapping table between active segments and resulting digits
        # convert the result into a number and add it to our end result
        sum += int(''.join([digits[''.join(sorted([str(segments.index(x)) for x in out]))] for out in output]))

    print(sum)

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        file_content = f.read().strip()
        task1(file_content)
        task2(file_content)

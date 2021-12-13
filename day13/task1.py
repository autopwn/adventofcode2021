#!/usr/bin/env python3
from collections import defaultdict

def printsheet(sheet, max_x, max_y):

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            print('#' if sheet[(x,y)] > 0 else ' ', end='')
        print()

def solve(data, task2 = False):

    sheet = defaultdict(int)
    points, instructions = data.split("\n\n")

    max_x = 0
    max_y = 0

    for point in [(int(x.split(',')[1]), int(x.split(',')[0])) for x in points.split("\n")]:
        sheet[point] = 1
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]

    for axis, position in [tuple(x.split()[2].split('=')) for x in instructions.split("\n")]:

        position = int(position)

        if axis == 'y':
            for dot, value in sheet.copy().items():
                if dot[0] > position and value > 0:
                    new_y = position - abs(position - dot[0])
                    sheet[(new_y,dot[1])] = 1
                    sheet.pop(dot, None)
            max_x = position

        if axis == 'x':
            for dot, value in sheet.copy().items():
                if dot[1] > position and value > 0:
                    new_x = position - abs(position - dot[1])
                    sheet[(dot[0], new_x)] = 1
                    sheet.pop(dot, None)
            max_y = position

        if not task2:
            print("Task 1 - Visible dots after first fold", sum([sheet[x] for x in sheet]))
            return

    print("Task 2: \n")
    printsheet(sheet, max_x, max_y)

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        solve(data)
        solve(data, True)

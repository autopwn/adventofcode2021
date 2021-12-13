#!/usr/bin/env python3
import numpy as np

with open('input.txt', 'r') as f:
    data = f.read().strip()

points, instructions = data.split("\n\n")
points = [(int(x.split(',')[1]), int(x.split(',')[0])) for x in points.splitlines()]
mx = max([x[0] for x in points]) + 1
my = max([x[1] for x in points]) + 1
a = np.zeros((mx, my), np.bool)
task1_done = False

for point in points:
    a[point[0]][point[1]] = True

for axis, position in [tuple(x.split()[2].split('=')) for x in instructions.split("\n")]:
    if axis == 'y':
        top, bottom = np.array_split(a, 2)
        a = np.logical_or(top[:-1], np.flipud(bottom))
    if axis == 'x':
        left, right = np.array_split(a, 2, 1)
        a = np.logical_or(left[:, :-1], np.fliplr(right))

for x in range(a.shape[0]):
    for y in range(a.shape[1]):
        print('#' if a[x][y] else ' ', end='')
    print()
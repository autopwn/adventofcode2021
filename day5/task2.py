#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  data = list(map(str.strip, f))

width, height = 1000, 1000
grid = [[0 for x in range(width)] for y in range(height)]

required_overlaps = 2
sufficient_overlaps = 0

for line in data:

  start, end = line.split(' -> ')

  start = list(map(int, start.split(',')))
  end = list(map(int, end.split(',')))

  for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
    for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
      # if not horizontal or vertical, check if point is on line
      if start[0] != end[0] and start[1] != end[1]:
          if abs(end[0] - i) != abs(end[1] - j):
            continue
      grid[j][i] += 1
      if grid[j][i] == required_overlaps:
        sufficient_overlaps += 1

print(sufficient_overlaps)

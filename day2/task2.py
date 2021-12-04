#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  lines = list(map(str.strip, f))

pos = [0,0]
aim = 0

for line in lines:
  cmd, unit = line.split(' ')
  if cmd == 'forward':
    pos[0] += int(unit)
    pos[1] += aim * int(unit)
  if cmd == 'down':
    aim += int(unit)
  if cmd == 'up':
    aim -= int(unit)

print(pos[0] * pos[1])
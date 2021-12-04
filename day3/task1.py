#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  lines = list(map(str.strip, f))
bits = len(lines[0])
counters = [[0 for i in range(2)] for j in range(bits)]
for line in lines:
  for bit in range(bits):
    if line[bit] == '0':
      counters[bit][0] += 1
    else:
      counters[bit][1] += 1
gamma = ''
epsilon = ''
for counter in counters:
  gamma += '0' if counter[0] > counter[1] else '1'
  epsilon += '1' if counter[0] > counter[1] else '0'
print(int(gamma, 2) * int(epsilon, 2))
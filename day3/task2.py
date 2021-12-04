#!/usr/bin/env python3
def get_rating(type: str):
  with open('input.txt', 'r') as f:
    lines = list(map(str.strip, f))
  bits = len(lines[0])
  for b1 in range(bits):
    c = [[0 for i in range(2)] for j in range(bits)]
    for line in lines:
      for b2 in range(bits):
        if line[b2] == '0':
          c[b2][0] += 1
        else:
          c[b2][1] += 1
    if type == 'oxygen generator':
      moco = '0' if c[b1][0] > c[b1][1] else '1'
    else:
      moco = '1' if c[b1][0] > c[b1][1] else '0'
    lines = [x for x in lines if x[b1] == moco]
    if len(lines) == 1:
      break
  return int(lines[0], 2)
print(get_rating('oxygen generator') * get_rating('co2 scrubber'))
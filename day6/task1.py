#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  data = list(map(str, f))

fishes = [int(x) for x in data[0].split(',')]

for i in range(80):
  for idx in range(len(fishes)):
    if fishes[idx] == 0:
      fishes.append(8)
      fishes[idx] = 6
    else:
      fishes[idx] -= 1

print(f"task 1: {len(fishes)}")
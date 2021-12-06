#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  data = list(map(str, f))

fishes = [int(x) for x in data[0].split(',')]

timers = [0,0,0,0,0,0,0,0,0]

for fish in fishes:
  timers[fish] += 1

for i in range(256):
  add_new = timers[0]
  reset = timers[0]
  for j in range(len(timers)-1):
    timers[j] = timers[j+1]
    if j == 6:
      timers[j] += reset
  timers[8] = add_new

print(f"task 2: {sum(timers)}")

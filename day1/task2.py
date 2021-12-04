#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  lines = list(map(int, f))

win_size = 3
count_increases = 0

for idx in range(1, len(lines)):
    last_win = sum(lines[idx-1:idx-1+win_size])
    current_win = sum(lines[idx:idx+win_size])
    if current_win > last_win:
        count_increases += 1

print(count_increases)
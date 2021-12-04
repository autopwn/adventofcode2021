#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  lines = list(map(int, f))

last_measurement = lines[0]
count_increases = 0

for measurement in lines:
  if measurement > last_measurement:
    count_increases += 1
  last_measurement = measurement

print(count_increases)
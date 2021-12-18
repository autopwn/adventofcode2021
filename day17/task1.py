#!/usr/bin/env python3
import re

def launch(tgt_min_x, tgt_max_x, tgt_min_y, tgt_max_y, s, v):
    my = -10000000000
    while True:
        s[0] += v[0]
        s[1] += v[1]
        v[0] = v[0] - 1 if v[0] > 0 else 0
        v[1] = v[1] - 1
        if s[0] >= tgt_min_x and s[0] <= tgt_max_x and s[1] >= tgt_min_y and s[1] <= tgt_max_y:
            return my
        if (v[0] == 0 and (s[0] < tgt_min_x or s[0] > tgt_max_x)) or (s[1] < min(tgt_min_y, tgt_max_y)):
            return None
        if s[1] > my:
            my = s[1]

def reverse_gauss(target):
    n = i = target
    while i > 0:
        i = i // 2 if i > 1 else 1
        t = n*(n+1)//2
        if t > target:
            n = n - i
        else:
            n = n + i
        if i == 1:
            while n*(n+1)//2 >= target:
                n -= 1
            return n+1

with open('input.txt', 'r') as f:
    data = f.read()

tgt_min_x, tgt_max_x, tgt_min_y, tgt_max_y = [int(n) for n in re.findall(r'-?\d+', data.strip())]

ymax = 0
hitcount = set()

# mostly guessed but it worked worked
miny = min(tgt_min_y, tgt_max_y)
maxy = abs(miny)

# Very doubtful saving of some iterations by calculating the mininum
# start for the outer loop
# -> get value of n so that n(n+1)//2 >= tgt_min_x
for x1 in range(reverse_gauss(tgt_min_x), tgt_max_x+1):
    for x2 in range(miny, maxy):
        r = launch(tgt_min_x, tgt_max_x, tgt_min_y, tgt_max_y, [0,0], [x1,x2])
        if r != None:
            if r > ymax:
                ymax = r
            hitcount.add((x1,x2))

print(f"Task 1 - highest y position: {ymax}")
print(f"Task 2 - distinct velocity values hitting target: {len(hitcount)}")

#!/usr/bin/env python3

def launch(tx, ty, s, v):
    my = -10000000000
    while True:
        s[0] += v[0]
        s[1] += v[1]
        v[0] = v[0] - 1 if v[0] > 0 else 0
        v[1] = v[1] - 1
        if s[0] >= tx[0] and s[0] <= tx[1] and s[1] >= ty[0] and s[1] <= ty[1]:
            return my
        if (v[0] == 0 and (s[0] < tx[0] or s[0] > tx[1])) or (s[1] < min(ty[0], ty[1])):
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
    data = f.read().strip()

tx, ty = [x.replace('=', '').replace('x','').replace('y','').replace(',','').split('..') for x in data.split(' ')[2:]]
tx = [int(tx[0]), int(tx[1])]
ty = [int(ty[0]), int(ty[1])]
best = min(ty)
count = set()

miny = min(ty)
maxy = abs(miny)

for x1 in range(reverse_gauss(tx[0]),tx[1]+1):
    for x2 in range(miny, maxy):
        r = launch(tx, ty, [0,0], [x1,x2])
        if r != None:
            if r > best:
                best = r
            count.add((x1,x2))

print(best, len(count))


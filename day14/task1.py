#!/usr/bin/env python3
from collections import Counter

with open('input.txt', 'r') as f:
    template, rules = f.read().strip().split("\n\n")

rules = {k:v for k,v in [x.split(" -> ") for x in rules.split("\n")]}

for _ in range(10):
    tmp = template[0]
    for i in range(len(template) - 1):
        tmp += rules[template[i:i+2]] + template[i+1]
    template = tmp

c = Counter(template).most_common()
print(c[0][1] - c[-1][1])

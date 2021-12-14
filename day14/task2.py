#!/usr/bin/env python3
from collections import Counter

with open('input.txt', 'r') as f:
    template, rules = f.read().strip().split("\n\n")

rules = {k:v for k,v in [x.split(" -> ") for x in rules.split("\n")]}
pairs = Counter()

for i in range(len(template) - 1):
    pairs[template[i:i+2]] += 1

for _ in range(40):
    for k, v in pairs.copy().items():
        pairs[k[0] + rules[k]] += v
        pairs[rules[k] + k[1]] += v
        pairs[k] -= v

x = Counter()
for k, v in pairs.items():
    x[k[1]] += v

mc = x.most_common()
result = mc[0][1] - mc[-1][1]

# whatever ?!?!?!?!
if template[0] == mc[-1][0]:
    result -= 1

print(result)
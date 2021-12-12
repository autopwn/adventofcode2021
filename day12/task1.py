#!/usr/bin/env python3
from collections import defaultdict

def find_paths(cave, redeemed_second = True, path = []):

    if cave == 'end':
        paths.add(tuple(path))
        return

    if cave.islower() and cave in path:
        if redeemed_second:
            return
        redeemed_second = True

    for adjacent in [c for c in caves[cave] if c != 'start']:
        find_paths(adjacent, redeemed_second, path + [cave])

with open('input.txt', 'r') as f:

    caves = defaultdict(set)
    for path_from, path_to in [x.split('-') for x in f.read().strip().split("\n")]:
        caves[path_to].add(path_from)
        caves[path_from].add(path_to)

    # task 1
    paths = set()
    find_paths('start')
    print(f"Task 1:  {len(paths)} paths")

    # task 2
    paths = set()
    find_paths('start', False)
    print(f"Task 2:  {len(paths)} paths")

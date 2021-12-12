#!/usr/bin/env python3
from collections import defaultdict

def find_paths(cave, second_visit = None, path = []):

    if cave.islower() and cave not in ['start', 'end'] and cave in path:
        if cave != second_visit:
            return
        second_visit = None

    if cave == 'end':
        paths.add(tuple(path))
        return

    for adjacent in [c for c in caves[cave] if c != 'start']:
        find_paths(adjacent, second_visit, path + [cave])

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
    for cave in caves:
        if cave.islower() and cave not in ['start', 'end']:
            find_paths('start', cave)
    print(f"Task 2:  {len(paths)} paths")

#!/usr/bin/env python3
class Cave:

    def __init__(self, name):
        self.name = name
        self.adjacent_caves = []

    def add_adjacent(self, cave):
        if not cave in self.adjacent_caves:
            self.adjacent_caves.append(cave)

    def get_adjacent(self):
        return self.adjacent_caves

    def is_small(self):
        return self.name not in ['start', 'end'] \
          and self.name.lower() == self.name

def solve(cave, second_visit = None, path = []):

    # dont visit small caves more than once 
    # except we have a joker (second_visit)
    if cave.is_small() and cave in path:
        if cave != second_visit:
            return
        second_visit = None

    # if we hit the end, we add this path as
    # a tuple to the paths set
    if cave.name == 'end':
        paths.add(tuple([x.name for x in path]))
        return

    for adjacent in cave.get_adjacent():
        if adjacent.name == 'start':
            continue
        solve(adjacent, second_visit, path + [cave])

with open('input.txt', 'r') as f:

    # Build cave tree
    caves = {}
    for line in f.read().strip().split("\n"):
        cfrom, cto= line.split('-')
        if cfrom not in caves:
            node = Cave(cfrom)
            caves[cfrom] = node
        if cto not in caves:
            node = Cave(cto)
            caves[cto] = node
        caves[cto].add_adjacent(caves[cfrom])
        caves[cfrom].add_adjacent(caves[cto])

    # task 1
    paths = set()
    solve(caves['start'])
    print(f"Task 1:  {len(paths)} paths")

    # task 2
    paths = set()
    for name, cave in caves.items():
        if len(name) not in ['start', 'end'] and name.lower() == name:
            solve(caves['start'], cave)
    print(f"Task 2:  {len(paths)} paths")

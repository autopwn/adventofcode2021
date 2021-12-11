#!/usr/bin/env python3
from aocutils.grid import Grid

def flash_rounds(octos):

    pending_flashes = True
    flashed = set()
    while pending_flashes:
        pending_flashes = False
        for pos, val in octos.iter():
            if val == 9 and pos not in flashed:
                flashed.add(pos)
                octos.set(pos, 0)
                for npos, nval in octos.iter_adjacent(pos):
                    if nval != 9 and (npos) not in flashed:
                        octos.inc(npos)
                        if nval == 8:
                            pending_flashes = True
    return flashed

def task1(octos):

    flashes = 0
    for step in range(100):
        flashed = flash_rounds(octos)
        flashes += len(flashed)
        for pos, _ in octos.iter():
            if pos not in flashed:
                octos.inc(pos)
    print(f"Total flashes after 100 steps: {flashes}")

def task2(octos):

    step = 0
    while True:
        step += 1
        flashed = flash_rounds(octos)
        if len(flashed) == octos.size:
            print(f"Octopuses flashed simultaneously at step {step}")
            return
        for pos, _ in octos.iter():
            if pos not in flashed:
                octos.inc(pos)

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        input = f.read()
        task1(Grid(input, True))
        task2(Grid(input, True))

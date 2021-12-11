#!/usr/bin/env python3
import sys

def iterate_neighbours(px, py, octos):

    for x in range(px - 1, px + 2):
        if x < 0 or x >= len(octos):
            continue
        for y in range(py - 1, py + 2):
            if (x == px and y == py) or (y < 0 or y >= len(octos[0])):
                continue
            yield x, y

def iterate_octos(octos):

    for x in range(len(octos)):
        for y in range(len(octos[0])):
            yield x, y

def flash_rounds(octos):

    pending_flashes = True
    flashed = set()
    while pending_flashes:
        pending_flashes = False
        for x, y in iterate_octos(octos):
            if octos[x][y] == 9 and (x,y) not in flashed:
                flashed.add((x,y))
                octos[x][y] = 0
                for nx, ny in iterate_neighbours(x, y, octos):
                    if octos[nx][ny] != 9 and (nx,ny) not in flashed:
                        octos[nx][ny] += 1
                        if octos[nx][ny] == 9:
                            pending_flashes = True
    return flashed

def task1(octos):

    flashes = 0
    for step in range(100):
        flashed = flash_rounds(octos)
        flashes += len(flashed)
        for x, y in iterate_octos(octos):
            if (x, y) not in flashed:
                octos[x][y] += 1
    print(f"Total flashes after 100 steps: {flashes}")

def task2(octos):

    num_octopuses = len(octos) * len(octos[0])
    step = 0

    while True:
        step += 1
        flashed = flash_rounds(octos)
        if len(flashed) == num_octopuses:
            print(f"Octopuses flashed simultaneously at step {step}")
            return
        for x in range(len(octos)):
            for y in range(len(octos[0])):
                if (x, y) not in flashed:
                    octos[x][y] += 1

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:

        lines = f.read().strip().split("\n")
        w = len(lines)
        h = len(lines[0])
        octos = [[0 for x in range(h)] for y in range(w)] 

        for x in range(w):
            for y in range(h):
                octos[x][y] = int(lines[x][y])
        task1(octos)

        for x in range(w):
            for y in range(h):
                octos[x][y] = int(lines[x][y])
        task2(octos)

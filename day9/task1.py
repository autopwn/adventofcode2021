#!/usr/bin/env python3
from functools import reduce

def iterate_neighbours(px, py, area):

    for x in range(px - 1, px + 2):
        if x < 0 or x >= len(area):
            continue
        for y in range(py - 1, py + 2):
            if ((x == px - 1 and y == py - 1) or (x == px + 1 and y == py + 1)) or (x == px - 1 and y == py + 1) or (x == px + 1 and y == py - 1):
                continue
            if (x == px and y == py) or (y < 0 or y >= len(area[0])):
                continue
            yield x, y

def check_neigbours(px, py, area):

    min = True
    for x,y in iterate_neighbours(px, py, area):
        if area[x][y] <= area[px][py]:
            min = False
    return int(area[px][py]) + 1 if min else 0

def find_basin(px, py, area, basin = set()):

    basin_size = 0
    for x,y in iterate_neighbours(px, py, area):
        if area[x][y] >= area[px][py] and area[x][y] != 9:
            basin_size += 1
            if (x, y) not in basin:
                basin.add((x, y))
                find_basin(x, y, area, basin)
        else:
            basin_size += 1
  
    return len(basin)

def task1(area):

    sum = 0
    for x in range(len(area)):
        row = [i for i in lines[x]]
        for y in range(len(area[0])):
            risk = check_neigbours(x, y, area)
            sum += risk
    print(sum)

def task2(area):

    basins = []
    for x in range(len(area)):
        row = [i for i in lines[x]]
        for y in range(len(area[0])):
            risk = check_neigbours(x, y, area)
            if risk > 0:
                basins.append(find_basin(x, y, area, {(x,y)}))
    print(reduce((lambda x, y: x * y), sorted(basins, reverse=True)[0:3])) 


with open('input.txt', 'r') as f:

    lines = f.read().strip().split("\n")
    w = len(lines)
    h = len(lines[0])
    area = [[0 for x in range(h)] for y in range(w)] 
    for x in range(w):
        row = [i for i in lines[x]]
        for y in range(h):
            area[x][y] = int(row[y])
    task1(area)
    task2(area)

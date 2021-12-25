#!/usr/bin/env python3

c = ['>', 'v']

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def p(floor, num_rows, num_cols):

    for row in range(num_rows):
        for col in range(num_cols):
            if floor[(row, col)] in [0,1]:
                print(c[floor[(row, col)]], end='')
            else:
                print('.', end='')
        print()
    print()

def task1(data):

    data = data.splitlines()
    num_rows = len(data)
    num_cols = len(data[0])
    floor = {}

    def add(p1, p2):
        return (
            p1[0] + p2[0] if p1[0] + p2[0] < num_rows else 0,
            p1[1] + p2[1] if p1[1] + p2[1] < num_cols else 0,
        )

    for row in range(num_rows):
        for col in range(num_cols):
            if data[row][col] in c:
                floor[(row, col)] = c.index(data[row][col])
            else:
                floor[(row, col)] = -1

    step = 0

    while True:
        step += 1
        count_moves = 0
        for idx, direction in enumerate([(0,1), (1,0)]):
            new_floor = floor.copy()
            for position, cucumber in floor.items():
                target = add(position, direction)
                if floor[position] == idx and floor[target] not in [0,1]:
                    new_floor[target] = floor[position]
                    new_floor[position] = ''
                    count_moves +=1
                floor = new_floor
        if count_moves == 0:
            break
 
    print(step)

def task2(data):
    pass

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        task1(data)
        task2(data)

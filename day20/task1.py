#!/usr/bin/env python3

def print_image(image, min_x, max_x, min_y, max_y):
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if (j,i) in image:
                print('#', end='')
            else:
                print('.', end='')
        print()

def iterate_neighbours(image, p):

    yield(p[0] - 1, p[1] - 1)
    yield(p[0], p[1] - 1)
    yield(p[0] + 1, p[1] - 1)

    yield(p[0] - 1, p[1])
    yield(p[0], p[1])
    yield(p[0] + 1, p[1])

    yield(p[0] - 1, p[1] + 1)
    yield(p[0], p[1] + 1)
    yield(p[0] + 1, p[1] + 1)

def new_pixel(image, p, algo):
    number = ''
    for i in iterate_neighbours(image, p):
        if i in image:
            number += '1'
        else:
            number += '0'
    number = int(number, 2)
    return algo[number]

def solve(data, iterations):
    algo, data = data.split("\n\n")
    algo = algo.replace("\n", "")
    data = data.splitlines()
    image = {}

    for y in range(len(data)):
        dd = [i for i in data[y]]
        for x in range(len(dd)):
            if dd[x] == '#':
                image[(x,y)] = 1

    min_x = min([x[0] for x in image])
    max_x = max([x[0] for x in image])
    min_y = min([x[1] for x in image])
    max_y = max([x[1] for x in image])

    for step in range(iterations):

        optimized_image = {}

        min_x -= 4
        max_x += 4
        min_y -= 4
        max_y += 4

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                pixel = new_pixel(image, (x,y), algo)
                if pixel == '#':
                    optimized_image[(x,y)] = 1

        image = optimized_image

        min_x += 3
        max_x -= 3
        min_y += 3
        max_y -= 3

        if step % 2 == 1:
            pl = list(image.keys())
            for p in pl:
                if p[0] < min_x or p[0] > max_x or p[1] < min_y or p[1] > max_y:
                    image.pop(p)

    print(f"Lit pixels after {iterations} iterations: {len(image)}")

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        solve(data, 2)
        solve(data, 50)

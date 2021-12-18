#!/usr/bin/env python3
from itertools import permutations
from math import floor, ceil
from copy import deepcopy

# Searches for a regular number to the left on the same depth level.
# If found, the top regular number from lstack is added.
def add_left(number, idx):

    global lstack

    for i in range(idx - 1, -1, -1):
        if isinstance(number[i], list):
            if add_left(number[i], len(number[i])):
                return True
        else:
            number[i] += lstack.pop()
            return True
    return False

# Searches for a regular number to the right on the same depth level.
# If found, the top regular number from lstack is added.
def add_right(number, idx) -> bool:

    global rstack

    for i in range(idx + 1, len(number)):
        if isinstance(number[i], list):
            if add_right(number[i], -1):
                return True
        else:
            number[i] += rstack.pop()
            return True
    return False

# Dives recursively into sublists and performns
# explode and split actions
def reduce(number, number_part = [], depth = 0):

    global action_occured
    global lstack
    global rstack
    global mode

    if not number_part:
        number_part = number

    # Explode action
    if mode == 0 and depth == 4:
        lstack.append(number_part[0])
        rstack.append(number_part[-1])
        action_occured = True
        return 0

    for i in range(len(number_part)):

        # Split action
        if mode == 1 and isinstance(number_part[i], int) and number_part[i] > 9:
            number_part[i] = [floor(number_part[i] / 2), ceil(number_part[i] / 2)]
            action_occured = True
            return number_part

        if isinstance(number_part[i], list):

            # Go deeper :)
            number_part[i] = reduce(number, number_part[i], depth + 1)

            # Try to add numbers from stack to neighbours,
            # otherwise they are kept for higher levels
            if action_occured:
                if len(lstack) > 0:
                    add_left(number_part, i)
                if len(rstack) > 0:
                    add_right(number_part, i)
                return number_part

    return number_part

# Repeated reduction of a single paired snailfish number
# until no more actions can be done
def reduce_pair(number):

    global lstack
    global rstack
    global action_occured
    global mode

    while True:

        at_least_one_action = False

        # First we do all possible explodes
        mode = 0
        while True:
            lstack = []
            rstack = []
            action_occured = False
            number = reduce(number)
            if action_occured:
                at_least_one_action = True
            if not action_occured:
                break

        # next we do at most one split
        # because we need to check for explodes after each split
        mode = 1
        lstack = []
        rstack = []
        action_occured = False
        number = reduce(number)
        if action_occured:
            at_least_one_action = True

        if not at_least_one_action:
            break

    return number

# Calculates the magnitute of a snailfish number
def get_mag(elem):
    mag = 0
    if isinstance(elem, int):
        mag += elem
    else:
        mag += 3 * get_mag(elem[0]) + 2 * get_mag(elem[1]) 
    return mag

def task1(data):

    # Iterate pairwise over input lines
    # For 3.10. see https://docs.python.org/3/library/itertools.html#itertools.pairwise :)
    lines = [eval(x) for x in data.splitlines()]
    for idx in range(1, len(data.splitlines())):
        number = [lines[idx - 1]] + [lines[idx]]
        lines[idx] = reduce_pair(number)
    
    print(f"Task 1 - magnitude of the final sum: {get_mag(number)}")

def task2(data):

    max_mag = 0

    for number in permutations([eval(line) for line in data.splitlines()],2):
        new_number = reduce_pair(deepcopy(list(number)))
        mag = get_mag(new_number)
        if mag > max_mag:
            max_mag = mag

    print(f"Task 2 - largest magnitude: {max_mag}")

if __name__ == "__main__":

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        task1(data)
        task2(data)

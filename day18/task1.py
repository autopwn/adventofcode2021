#!/usr/bin/env python3
from math import floor, ceil
from os import register_at_fork

def add_to_first_number_left(number, idx):

    global lstack

    for i in range(idx - 1, -1, -1):
        if isinstance(number[i], list):
            if add_to_first_number_left(number[i], len(number[i])):
                return True
        else:
            number[i] += lstack.pop()
            return True
    return False

def add_to_first_number_right(number, idx) -> bool:

    global rstack

    for i in range(idx + 1, len(number)):
        if isinstance(number[i], list):
            if add_to_first_number_right(number[i], -1):
                return True
        else:
            number[i] += rstack.pop()
            return True
    return False

def is_pair(item):

    return isinstance(item, list) \
        and len(item) == 2 \
        and isinstance(item[0], int) \
        and isinstance(item[1], int)

def stacks():

    global lstack
    global rstack

    return f"[l:{lstack},r:{rstack}]"

#
# [[[[[9,8],1],2],3],4]
#
def reduce(number, number_part = [], depth = 0):

    global action_occured
    global lstack
    global rstack
    global mode

    if not number_part:
        number_part = number

    if mode == 0 and depth == 4:
        if not is_pair(number_part):
            raise AssertionError("Non-pair at depth 4!")
        lstack.append(number_part[0])
        rstack.append(number_part[-1])
        action_occured = True
        return 0

    for i in range(len(number_part)):

        if mode == 1 and isinstance(number_part[i], int) and number_part[i] > 9:
            if action_occured:
                raise AssertionError("KKK")
            print("SPLIT")
            number_part[i] = [floor(number_part[i] / 2), ceil(number_part[i] / 2)]
            action_occured = True
            return number_part

        if isinstance(number_part[i], list):

            if action_occured:
                raise AssertionError("BUBU")

            number_part[i] = reduce(number, number_part[i], depth + 1)

            if action_occured:
                if len(lstack) > 0:
                    add_to_first_number_left(number_part, i)
                    print("after add_to_first_number_left", number_part, stacks())
                if len(rstack) > 0:
                    add_to_first_number_right(number_part, i)
                    print("after add_to_first_number_right", number_part, stacks())
                return number_part

    return number_part

def explode(number, number_part, depth = 0):

    print(id(number))

    global action_occured
    global lstack
    global rstack

    if action_occured:
        print("JJJ")
        exit()

    if depth == 4 and not action_occured:
        lstack.append(number_part[0])
        rstack.append(number_part[-1])
        action_occured = True
        print("EXPLODED", number_part, lstack, rstack, action_occured)
        return 0

    for i in range(len(number_part)):

        if isinstance(number_part[i], int) and number_part[i] > 9:
            print("SPLIT")
            number_part[i] = [floor(number_part[i] / 2), ceil(number_part[i] / 2)]
            action_occured = True
            #return number_part

        if isinstance(number_part[i], list) and not action_occured:

            part = explode(number_part[i], depth + 1)

            if (len(lstack)) > 0:
                print("  before add_to_first_number_part_left", number_part)
                add_to_first_number_part_left(number_part, i)
                print("  after add_to_first_number_part_left", number_part, lstack)

            # Then, the entire exploding pair is replaced with the regular number_part 0.
            number_part[i] = part
        
        if action_occured:
            print("ABORT AFTERT ACTION", lstack, rstack)

    return number_part

def task1(data):

    global lstack
    global rstack
    global action_occured
    global mode

    lstack = []
    rstack = []
    action_occured = False

    lines = [eval(x) for x in data.splitlines()]

    for idx in range(1, len(data.splitlines())):

        number = [lines[idx - 1]] + [lines[idx]]

        print("NUMBERS", number)

        while True:

            at_least_one_action = False

            # first we do all possible explodes
            mode = 0
            while True:
                lstack = []
                rstack = []
                action_occured = False
                number = reduce(number)
                if action_occured:
                    at_least_one_action = True
                print("After action", str(number).replace(" ", ""), lstack, rstack)
                if not action_occured:
                    break

            # next we do at most one split, because we need to check for explodes after each split
            mode = 1
            lstack = []
            rstack = []
            action_occured = False
            number = reduce(number)
            if action_occured:
                at_least_one_action = True
            print("After action", str(number).replace(" ", ""), lstack, rstack)

            if not at_least_one_action:
                break

        lines[idx] = number
    
    print(str(number).replace(" ", ""))

def task2(data):
    pass

if __name__ == "__main__":

    example = 1

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        task1(data)
        task2(data)

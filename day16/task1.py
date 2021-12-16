#!/usr/bin/env python3
#from aocutils.bfs import BreadthFirstSearch
#from aocutils.grid import Grid
#import sys

from functools import reduce
from operator import mul

operators = {
    0: '+',
    1: '*',
    2: 'min',
    3: 'max',
    5: '>',
    6: '<',
    7: '='
}

tr = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

def parse_literal(packet):

    numbits = ''
    while len(packet) >= 5:
        if packet[0] == '1':
            numbits += packet[1:5]
            packet = packet[5:]
        else:
            numbits += packet[1:5]
            packet = packet[5:]
            return packet, int(numbits, 2)

def parse(packet):

    global version_sum
    global stack

    version = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)

    version_sum += version

    #print("TYPE", type_id )

    packet = packet[6:]

    if type_id == 4:
        packet, value = parse_literal(packet)
        stack.append(value)
    else:
        length_type_id = int(packet[0], 2)
        if length_type_id == 0:
            subpacket_length = int(packet[1:16], 2)
            packet = packet[16:]
        elif length_type_id == 1:
            subpacket_count = int(packet[1:12], 2)
            packet = packet[12:]
        else:
            raise AssertionError("WHAT TO DO HERE?")

        #if operators[type_id] == '>':
        #    breakpoint()
        stack.append(operators[type_id])

        packet = parse(packet)

        if not stack:
            raise AssertionError("EMPTY STACK")

    if packet and int(packet, 2) != 0:
        packet = parse(packet)
    else:
        return packet

def consume_operands(operand_stack):

    # when # is top
    if len(operand_stack) > 0 and operand_stack[-1] == '#':
        operand_stack.pop()

    tmp_operands = []
    while len(operand_stack) > 0:
        op = operand_stack.pop()
        if op == '#':
            return tmp_operands
        tmp_operands.append(op)
    return tmp_operands

def process_stack():
    
    global stack

    operand_stack = []

    for elem in reversed(stack):

        if elem not in operators.values():
            operand_stack.append(elem)
        else:
            if elem == '+':
                operand_stack.append(sum(consume_operands(operand_stack)))
                operand_stack.append('#')
            elif elem == '*':
                operand_stack.append(reduce(mul, consume_operands(operand_stack), 1))
                operand_stack.append('#')
            elif elem == 'min':
                operand_stack.append(min(consume_operands(operand_stack)))
                operand_stack.append('#')
            elif elem == 'max':
                operand_stack.append(max(consume_operands(operand_stack)))
                operand_stack.append('#')
            elif elem == '<':
                op1, op2 = consume_operands(operand_stack)
                operand_stack.append(1 if op2 > op1 else 0)
                operand_stack.append('#')
            elif elem == '>':
                #print("-----", operand_stack)
                op1, op2 = consume_operands(operand_stack)
                operand_stack.append(1 if op1 > op2 else 0)
                operand_stack.append('#')
            elif elem == '=':
                op1, op2 = consume_operands(operand_stack)
                #print("EQU", op1, op2)
                operand_stack.append(1 if op1 == op2 else 0)
                operand_stack.append('#')

        #print(stack, operand_stack)
    
    return consume_operands(operand_stack)[0]

def task1(data):

    binstr = ''.join([tr[x] for x in data])

    global version_sum
    version_sum = 0

    global stack
    stack = []

    parse(binstr)

    return version_sum, process_stack()

def task2(data):
    pass

if __name__ == "__main__":

    example = 0

    assert(task1('C200B40A82') == (14, 3))
    assert(task1('04005AC33890') == (8, 54))
    assert(task1('880086C3E88112') == (15, 7))
    assert(task1('CE00C43D881120') == (11, 9))
    assert(task1('D8005AC2A8F0') == (13, 1))
    assert(task1('F600BC2D8F') == (19, 0))
    assert(task1('9C005AC2F8F0') == (16, 0))
    assert(task1('9C0141080250320F1802104A08') == (20, 1))

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()

        task1(data)

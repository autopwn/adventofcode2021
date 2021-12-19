#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations, permutations
from itertools import product
from collections import Counter
from math import sqrt

def get_vector(b1, b2):
    return (b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2])

def vec_len(vector):
    return sqrt( vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2] )
    #return abs(vector[0]) + abs(vector[1]) + abs(vector[2])

def rotate_x(vec, r = 0):
    if r == 0: return  vec
    if r == 90: return (vec[0], -vec[2], vec[1])
    if r == 180: return (vec[0], -vec[1], -vec[2])
    if r == 270: return (vec[0], vec[2], -vec[1])
    raise AssertionError("Invalid rotation")

def rotate_y(vec, r = 0):
    if r == 0: return  vec
    if r == 90: return (-vec[2], vec[1], vec[0])
    if r == 180: return (-vec[0], vec[1], -vec[2])
    if r == 270: return (vec[2], vec[1], -vec[0])
    raise AssertionError("Invalid rotation")

def rotate_z(vec, r = 0):
    if r == 0: return  vec
    if r == 90: return (-vec[1], vec[0], vec[2])
    if r == 180: return (-vec[0], -vec[1], vec[2])
    if r == 270: return (vec[1], -vec[0], vec[2])
    raise AssertionError("Invalid rotation")

def rotate(vec, orientation):
    return rotate_z(rotate_y(rotate_x(vec, orientation[0]), \
        orientation[1]), orientation[2])

def calculate_rotation_matches(vec1, vec2):

    res = set()
    x = y = z = 0
    for x in (0,90,180,270):
        for y in (0,90,180,270):
            for z in (0,90,180,270):
                vec = rotate(vec1, (x,y,z)) 
                if vec == vec2:
                    #print("Match", vec, vec2, (x,y,z))
                    res.add((x,y,z))
    return res

def compare_scanners(s1, s2):

    orientation_counter = Counter()

    matches = defaultdict(Counter)

    for s1p1 in s1:
        for s1p2 in s1:
            if s1p1 == s1p2:
                continue
            v_s1p1_s1p2 = get_vector(s1p1, s1p2)
            l_v_s1p1_s1p2 = vec_len(v_s1p1_s1p2)

            for s2p1 in s2:
                for s2p2 in s2:
                    if s2p1 == s2p2:
                        continue
                    v_s2p1_s2p2 = get_vector(s2p1, s2p2)
                    l_v_s2p1_s2p2 = vec_len(v_s2p1_s2p2)

                    # vectors of both scanner have same length
                    if l_v_s1p1_s1p2 == l_v_s2p1_s2p2:
                        # try to correctly orientate vectors
                        orientations = calculate_rotation_matches(v_s1p1_s1p2, v_s2p1_s2p2)
                        if len(orientations) > 0:
                            #print("MAYBE MATCHING", s1p1, s1p2, s2p1, s2p2)
                            matches[s1p1][s2p1] += 1
                            for o in orientations:
                                orientation_counter[o] += 1

    print(orientation_counter.most_common(1))
    
    for ms1, ms2 in matches.items():
        print(ms1, ms2.most_common(1))

    exit()
    all_vectors_s1 = [(x[0], x[1]) for x in permutations(s1,2)]
    all_vectors_s2 = [(x[0], x[1]) for x in permutations(s2,2)]

    print(all_vectors_s1)
    exit()

    for v1 in all_vectors_s1:
        for v2 in all_vectors_s2:
            c = v1.calculate_rotation_matches(v2)
            exit()
            if c:
                print(c, v1, v2)
                exit()
                for cc in c:
                    counter[cc] += 1

    print("FOO")
    return counter.most_common(1)

def task1(data):

    scanners = []

    for scanner, beacons in [(int(y[0].split(' ')[2]), \
        [tuple([int(w) for w in z.split(',')]) \
        for z in y[1:]]) for y in [x.split("\n") for x in data.split("\n\n")]]:

        scanners.append(beacons)

    #print(list([len(x) for x in scanners]))

    compared = compare_scanners(scanners[0], scanners[1])
    #print(compared)

    # s0 -> s1 [((0, 180, 0), 132)]

    #print(get_vector((-618,-824,-621), (-537,-823,-458)))

    #print(rotate(get_vector((686,422,578), (605,423,415)), (0, 180, 0)))

    #for b in scanners[1]:
    #    print(rotate(b, (0, 180, 0)))

    # compared = compare_scanners(scanners[0], scanners[2])
    # print(compared)

    # compared = compare_scanners(scanners[0], scanners[3])
    # print(compared)

    # compared = compare_scanners(scanners[0], scanners[4])
    # print(compared)

    # compared = compare_scanners(scanners[1], scanners[2])
    # print(compared)

    # compared = compare_scanners(scanners[1], scanners[3])
    # print(compared)

    # compared = compare_scanners(scanners[1], scanners[4])
    # print(compared)

    # compared = compare_scanners(scanners[2], scanners[3])
    # print(compared)

    # compared = compare_scanners(scanners[2], scanners[4])
    # print(compared)

    # compared = compare_scanners(scanners[3], scanners[4])
    # print(compared)

def task2(data):
    pass

if __name__ == "__main__":

    example = 1

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        task1(data)
        task2(data)

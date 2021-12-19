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
    if r == 90: return (vec[2], vec[1], -vec[0])
    if r == 180: return (-vec[0], vec[1], -vec[2])
    if r == 270: return (-vec[2], vec[1], vec[0])
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

def rotate_reverse(vec, orientation):
    return rotate_x(rotate_y(rotate_z(vec, (360 - orientation[2]) % 360), \
        (360 - orientation[1]) % 360), (360 - orientation[0]) % 360)

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
                    # vectors of both scanner have same length
                    if l_v_s1p1_s1p2 == vec_len(v_s2p1_s2p2):
                        # try to correctly orientate vectors
                        orientations = calculate_rotation_matches(v_s1p1_s1p2, v_s2p1_s2p2)
                        if len(orientations) > 0:
                            matches[s1p1][s2p1] += 1
                            for o in orientations:
                                orientation_counter[o] += 1

    filtered_matches = []

    for ms1, ms2 in matches.items():
        filtered_matches.append((ms1, ms2.most_common(1)[0][0]))

    if len(filtered_matches) < 12:
        return None, None

    return filtered_matches, orientation_counter.most_common(1)[0][0]
    #return filtered_matches, orientation_counter.most_common(2)[1][0]

def task1(data):

    scanners = []
    beacons_seen_from_s1 = []

    for scanner, beacons in [(int(y[0].split(' ')[2]), \
        [tuple([int(w) for w in z.split(',')]) \
        for z in y[1:]]) for y in [x.split("\n") for x in data.split("\n\n")]]:

        scanners.append(beacons)

    # beacons seen by base scanner
    beacons_seen_from_s1 += scanners[0]

    for s1, s2 in combinations(range(len(scanners)), 2):

        matches, orientation = compare_scanners(scanners[s1], scanners[s2])

        if matches != None:
            print(f"Scanners {s1} and {s2} overlapp with orientation {orientation}")

            mc = Counter()

            for match_s1, match_s2 in matches:
                #print(match_s1, match_s2, orientation)
                #print(f"match_s1: {match_s1}")
                #print(f"match_s2: {match_s2}")
                s2_reorientated = rotate_reverse(match_s2, orientation)
                #s2_reorientated = rotate_reverse(match_s2, orientation)
                #print(match_s1, match_s2, s2_reorientated)
                #print(f"s2_reorientated: {s2_reorientated}")
                s2_from_pov_of_s1 = (match_s1[0] - s2_reorientated[0], match_s1[1] - s2_reorientated[1], match_s1[2] - s2_reorientated[2])
                #print(f"s2_from_pov_of_s1: {s2_from_pov_of_s1}\n")
                mc[s2_from_pov_of_s1] += 1

            if mc.most_common(1)[0][1] < 12:
                print("WRONG ROTATION", orientation)
            else:
                print(f"s2_from_pov_of_s1: {mc.most_common(1)[0][0]}\n")

            # v_s1_s2 = (68, -1246, -43)
            
            # for s2p in scanners[s2]:
            #     t = rotate_reverse(s2p, (0, 180, 0))
            #     tt = (v_s1_s2[0] + t[0], v_s1_s2[1] + t[1], v_s1_s2[2] + t[2])
            #     beacons_seen_from_s1.append(tt)

            # print(beacons_seen_from_s1)
            # print(len(beacons_seen_from_s1))
            # print(len(set(beacons_seen_from_s1)))

            # exit()
        #print("----------------------------\n")


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

    example = 0

    with open('example.txt' if example else 'input.txt', 'r') as f:
        data = f.read().strip()
        task1(data)
        task2(data)

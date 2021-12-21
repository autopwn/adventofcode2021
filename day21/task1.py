#!/usr/bin/env python3
dice_vals = {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}
calculated = {}

class Player():
    def __init__(self, id, position):
        self.id = id
        self.position = position - 1
        self.score = 0

    def move(self, moves):
        self.position = (self.position + moves) % 10
        self.score += self.position + 1
        return self.score 

    def __repr__(self):
        return f"({self.id}, {self.position+1}, {self.score})"

class Dice():
    def __init__(self):
        self.result = 0
        self.counter = 0

    def roll(self):
        self.counter += 1
        self.result += 1
        return self.result

def universe(position1, position2, score1, score2, to_move = 1):

    wp1 = 0
    wp2 = 0

    for value, count in dice_vals.items():
        if to_move == 1:
            wpn1 = (position1 - 1 + value) % 10 + 1
            score1_next = score1 + wpn1
            if score1_next >= 21:
                wp1 += count
            else:
                if (wpn1, position2, score1_next, score2, 3-to_move) in calculated:
                    wp1_sub, wp2_sub = calculated[(wpn1, position2, score1_next, score2, not 3-to_move)]
                else:
                    wp1_sub, wp2_sub = universe(wpn1, position2, score1_next, score2, 3-to_move)
                    calculated[(wpn1, position2, score1_next, score2, not 3-to_move)] = (wp1_sub, wp2_sub)
                wp1 += wp1_sub * count
                wp2 += wp2_sub * count
        else:
            wpn2 = (position2 - 1 + value) % 10 + 1
            score2_next = score2 + wpn2
            if score2_next >= 21:
                wp2 += count
            else:
                if (position1, wpn2, score1, score2_next, 3-to_move) in calculated:
                    wp1_sub, wp2_sub = calculated[(position1, wpn2, score1, score2_next, 3-to_move)]
                else:
                    wp1_sub, wp2_sub = universe(position1, wpn2, score1, score2_next, 3-to_move)
                    calculated[(position1, wpn2, score1, score2_next, 3-to_move)] = (wp1_sub, wp2_sub)
                wp1 += wp1_sub * count
                wp2 += wp2_sub * count

    return wp1, wp2

with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()

# Part 1
dice = Dice()
p1 = Player(int(data[0][7]), int(data[0][28:]))
p2 = Player(int(data[1][7]), int(data[1][28:]))

for _ in range(200):
    p1.move(sum([dice.roll(), dice.roll(), dice.roll()]))
    if p1.score >= 1000:
        print("Part 1:", p2.score * dice.counter)
        break
    p2.move(sum([dice.roll(), dice.roll(), dice.roll()]))
    if p2.score >= 1000:
        print("Part 1:", p1.score * dice.counter)
        break

# Part 2
result = max(universe(
    int(data[0][28:]),
    int(data[1][28:]),
    0, 0
))

print("Task 2:", result)

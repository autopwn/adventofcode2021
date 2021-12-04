#!/usr/bin/env python3
with open('input.txt', 'r') as f:
  lines = list(map(str.strip, f))

numbers = lines[0].split(',')

class Board:

  def __init__(self, input):

    self.board = []
    for line in input:
      [ self.board.append(x) for x in line.split() ]
    self.marks = [False] * len(self.board)

  def print(self):
    for i in range(len(self.board)):
      if i > 0 and i % 5 == 0:
        print()
      print(('[' + self.board[i] + ']' if self.marks[i] else self.board[i]) + ' ', end='')

  def draw(self, number):
    for idx in range(len(self.board)):
      if self.board[idx] == number:
        self.marks[idx] = True
    if self.checkwin():
      print(self.score(int(number)))
      exit()
  
  def score(self, number):

    score = 0
    for idx in range(len(self.board)):
      if self.marks[idx] != True:
        score += int(self.board[idx])
    return score * number

  def checkwin(self):
    # cols
    for i in range(5):
      sum = 0
      for y in range(5):
        if self.marks[i+y*5] == True:
          sum += 1
      if sum == 5:
        #print("WIN COL")
        return True
    # rows
    for i in range(5):
      sum = 0
      for y in range(5):
        if self.marks[y+i*5] == True:
          sum += 1
      if sum == 5:
        #print("WIN ROW")
        return True

boards = []

for i in range(2, len(lines), 6):
  board = Board(lines[i:i+5])
  boards.append(board)

for number in numbers:
  [ x.draw(number) for x in boards ]

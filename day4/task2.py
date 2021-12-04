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
    self.won = False
    self.score = 0

  def print(self):
    for i in range(len(self.board)):
      if i > 0 and i % 5 == 0:
        print()
      print(("\033[32;1m" + self.board[i].rjust(2, ' ') + "\033[0m" if self.marks[i] else self.board[i].rjust(2, ' ')) + ' ', end='')
    print()

  def draw(self, number):

    for idx in range(len(self.board)):
      if self.board[idx] == number:
        self.marks[idx] = True

    self.calculate_score(number)

    if self.checkwin():
      self.won = True
  
  def calculate_score(self, number):

    score = 0
    for idx in range(len(self.board)):
      if self.marks[idx] != True:
        score += int(self.board[idx])
    self.score = score * int(number)

  def checkwin(self):

    # cols
    for i in range(5):
      sum = 0
      for y in range(5):
        if self.marks[i+y*5] == True:
          sum += 1
      if sum == 5:

        return True

    # rows
    for i in range(5):
      sum = 0
      for y in range(5):
        if self.marks[y+i*5] == True:
          sum += 1
      if sum == 5:
        return True

boards = []

for i in range(2, len(lines), 6):
  board = Board(lines[i:i+5])
  boards.append(board)

last_score = 0
for number in numbers:
  [ x.draw(number) for x in boards ]
  if len(boards) == 1:
    last_score = boards[0].score
  boards = [x for x in boards if not x.won]
  if len(boards) == 0:
    print(last_score)
    exit()

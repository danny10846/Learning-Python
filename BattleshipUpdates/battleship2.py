from random import randint

board = [] 

#for loop to go from 0 to 5, 
for x in range(5):
  board.append(["O"] * 5)

#Function to get rid of commas and '', joins the string together inside " "
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

class BattleShip(object):

  def __init__(self, name, alignment, length):

    self.name = name
    self.alignment = alignment
    self.length = length
    self.start_row = randint(0, len(board) - 1)
    self.start_col = randint(0, len(board[0]) - 1)
    self.coords = [[start_row, start_col]]


  def lengthChange(self):

    if self.length > 4:
      self.length = 4

    if self.alignment == 1:
      if self.shipLength > ((len(board) - 1) - self.start_col):
        self.shipLength = ((len(board) -1) - self.start_col)

    if self.alignment == 2:
      if self.shipLength > ((len(board) - 1) - self.start_row):
        self.shipLength = ((len(board) -1) - self.start_row)


  def addShips(self):

    for i in range(0, self.shipLength+1):
      self.coords.append([start_row, start_col + i])



    

    
from random import randint

#board and ship lists
board = []
ship = []

#Initial variables we'll be using 
horizontal = 0
vertical = 0
shipLength = 0
hitCounter = 0

#for loop to go from 0 to 5, 
for x in range(5):
  board.append(["O"] * 5)

#Function to get rid of commas and '', joins the string together inside " "
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)


#determine whether the battleship is horizontal or vertical
if randint(1,2) == 1:
  horizontal = 1
else:
  vertical = 1

#initial position of start of ship
start_row = randint(0, len(board) - 1)
start_col = randint(0, len(board[0]) - 1)

#add initial to ship list as a set of coords in a list
ship.append([start_row, start_col])

#if horizontal, generate a ship length, make sure length will fit on board
if horizontal == 1:
  shipLength = randint(1,3)
  if shipLength > ((len(board) - 1) - start_col):
    shipLength = ((len(board) -1) - start_col)
  

  for i in range(1, shipLength+1):
    ship.append([start_row, start_col + i])

#else vertical
else:
  shipLength = randint(1,3)
  if shipLength > ((len(board) - 1) - start_row):
    shipLength = ((len(board) - 1) - start_row)

  for i in range(1, shipLength+1):
    ship.append([start_row + i, start_col])

#for 8 turns, user tries to sink the entire ship
for turn in range(8):
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))

        guess_list = [guess_row, guess_col]

        #if off booard, throw 'error'
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
          print "Oops, that's not even in the ocean."
        else:
          #if coords are in ship list coords, it's a hit
          if(guess_list in ship):
            board[guess_row][guess_col] = "B"
            print "It's a hit!"
            hitCounter += 1
          #or if guessed a previous guess 
          elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "1"):
            print "You guessed that one already."
          #else you missed 
          else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        
        #if ship length is reached, user wins
        if hitCounter == shipLength + 1:
          print "You win!"
          print_board(board)
          break

        #if 8 turns are reached, they lose
        if turn == 8:
          print "Game Over"
          print "Turn", turn + 1
        print_board(board)



from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(x):
    return randint(0, len(x) - 1)

def random_col(y):
    return randint(0, len(y[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

for turn in range(5):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row >= 0 or guess_row <= len(board) or guess_col >= 0 or guess_col <= len(board[0]):
        if ship_row == guess_row and ship_col == guess_col:
            board[int(guess_row)][int(guess_col)] = "!"
            print_board(board)
            print "Congratulations! You sank my battleship!"
            break
        else:
            print "You missed my battleship!"
            board[int(guess_row)][int(guess_col)] = "X"
    else: 
        print "Oops, that's not even in the ocean."

    if turn == 4:
        print "You lose!"
        break
    print_board(board)


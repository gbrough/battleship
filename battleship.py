from random import randint

#initializing board
board = []

print('A B C D E F G H')
for x in range(8):
    board.append(["O"] * 8)

def print_board(board):
    for row in board:
        print(" ".join(row))


#starting the game and printing the board
print_board(board)

#defining where the ship is
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#asking the user for a guess
turns = 1
while turns <= 5:
    print("Let's play Battleship!")
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    # if the user's right, the game ends
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        #warning if the guess is out of the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        
        #warning if the guess was already made
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        
        #if the guess is wrong, mark the point with an X and start again
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        

        # Print turn and board again here
        print("Turn " + str(turns) + " out of 4.")
        turns += 1
        print_board(board)

#if the user have made 4 tries, it's game over
if turns == 5:
    print("Game Over")
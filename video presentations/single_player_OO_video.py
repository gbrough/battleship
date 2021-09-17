import random

class GameBoard:
  def __init__(self, board):
    self.board = board

  def get_letters_to_numbers():
    letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    return letters_to_numbers

  def print_board(self):
      print("  A B C D E F G H")
      print("  +-+-+-+-+-+-+-+")
      row_number = 1
      for row in self.board:
          print("%d|%s|" % (row_number, "|".join(row)))
          row_number += 1

class Battleship:
  def __init__(self, board):
    self.board = board

  def create_ships(self):
    for i in range(5):
      self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
      while self.board[self.x_row][self.y_column] == "X":
        self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
      self.board[self.x_row][self.y_column] = "X"
    return self.board

  def get_user_input(self):
    try:
      x_row = input("Enter the row of the ship: ")
      while x_row not in '12345678':
          print('Not an appropriate choice, please select a valid row')
          x_row = input("Enter the row of the ship: ")

      y_column = input("Enter the column letter of the ship: ").upper()
      while y_column not in "ABCDEFGH":
          print('Not an appropriate choice, please select a valid column')
          y_column = input("Enter the column letter of the ship: ").upper()
      return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
    except ValueError and KeyError:
      print("Not a valid input")
      return self.get_user_input()

  def count_hit_ships(self):
    hit_ships = 0
    for row in self.board:
      for column in row:
        if column == "X":
          hit_ships += 1
    return hit_ships

def RunGame(): 
  computer_board = GameBoard([[" "] * 8 for i in range(8)])
  user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
  Battleship.create_ships(computer_board)
  #start 10 turns
  turns = 10
  while turns > 0:
    GameBoard.print_board(user_guess_board)
    #get user input
    user_x_row, user_y_column = Battleship.get_user_input(object)
    #check if duplicate guess
    while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
      print("You guessed that one already")
      user_x_row, user_y_column = Battleship.get_user_input(object)
    #check for hit or miss
    if computer_board.board[user_x_row][user_y_column] == "X":
      print("You sunk 1 of my battleship!")
      user_guess_board.board[user_x_row][user_y_column] = "X"
    else:
      print("You missed my battleship!")
      user_guess_board.board[user_x_row][user_y_column] = "-"
    #check for win or lose
    if Battleship.count_hit_ships(user_guess_board) == 5:
      print("You hit all 5 battleships!")
      break
    else:
      turns -= 1
      print(f"You have {turns} turns remaining")
      if turns == 0:
        print("Sorry you ran out of turns")
        GameBoard.print_board(user_guess_board)
        break

if __name__ == '__main__':
  RunGame()
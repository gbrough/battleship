from random import randint  

class Player:
  def __init__(self, name, board):
      self.name = name
      self.board = board
  def create_players(self):
      self.user = Player("User", GameBoard())
      self.computer = Player("Computer", GameBoard())
class GameBoard:
  def __init__(self, column):
      self.board = []
      self.column = column
  def create_board(board):
    board = [[" "] * 8 for i in range(8)]
  def convert(self, column):
    letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
    }
    return letters_to_numbers[column]
  def print_board(self):
      print("  A B C D E F G H")
      print("  +-+-+-+-+-+-+-+")
      row_number = 1
      for row in self.board:
          print("%d|%s|" % (row_number, "|".join(row)))
          row_number += 1
class Battleship(object):
  def __init__(self, board, row, column):
    self.board = board
    self.row = row
    self.column = column

  def get_ship_location(row, column):
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, GameBoard.convert.letters_to_numbers[column]

  def create_ships(board, row, column):
    for ship in range(5):
      row, column = randint(0,7), randint(0,7)
      while board[row[column] == "X":
        row, column = randint(0,7), randint(0,7)
      board[row[column] = "X"
      print(self.board)

def run():

  
if __name__ == '__main__':
  run()







  






import random
class Player:
  def __init__(self, name):
      self.name = name
  def get_name(self):
      return self.name

class GameBoard:
  def __init__(self, board):
    self.board = board
  #     self.column = column
  def create_board(self):
    self.board = [[" "] * 8 for i in range(8)]

  def print_board(self):
      print("  A B C D E F G H")
      print("  +-+-+-+-+-+-+-+")
      row_number = 1
      for row in self.board:
          print("%d|%s|" % (row_number, "|".join(row)))
          row_number += 1
class Battleship():
  def __init__(self, board):
    self.board = board

  def create_ships(self):
    for ship in range(5):
      self.row, self.column = random.randint(0, 7), random.randint(0, 7)
      self.board[self.row][self.column] = "X"
    return self.board
  
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

  def get_ship_location(self):
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, self.letters_to_numbers[column]

class RunGame():
  def __init__(self):
    user1 = Player("Garrett")
    user2 = Player("Computer")
    print(Player.get_name(user1), Player.get_name(user2))
    input = Battleship.get_ship_location()
    print(input)
    user1_board = GameBoard.create_board()
    print(GameBoard.print_board(user1_board))

if __name__ == '__main__':
  RunGame()







  






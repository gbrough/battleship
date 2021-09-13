class Battleship(object):
  def __init__(self, board, row, column, length, direction):
    self.board = board
    self.row = row
    self.column = column
    self.length = length
    self.direction = direction

  def place_ship(self, board, row, column, length, direction):
    for i in range(length):
        if direction == "N":
            el = (row[0], column[1] - i)
            board.add_ship(el)
        elif direction == "S":
            el = (row[0], column[1] + i)
            board.add_ship(el)
        elif direction == "W":
            el = (row[0] - i, column[1])
            board.add_ship(el)
        elif direction == "E":
            el = (row[0] + i, column[1])
            board.add_ship(el)
        else:
            print("Wrong direction")
            return False

class board:
  def __init__(self):
      self.board = []
  board = [[" "] * 8 for i in range(8)]
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
  def print_board(self):
      print("  0 1 2 3 4 5 6 7")
      for i in range(8):
          print(i, end=" ")
          for j in range(8):
              print(self.board[i][j], end=" ")
          print()

class Player:
  def __init__(self, name, board):
      self.name = name
      self.board = board

def run():
  user_board = board()
  user = Player("user", user_board)
  computer = Player("Computer",(8, 8))
  #place battleships
  Battleship.place_ship(user_board, 0, 0, 5, 'E')
  Battleship.place_ship(user_board, 1, 0, 4, 'E')
  Battleship.place_ship(user_board, 2, 0, 3, 'E')
  Battleship.place_ship(user_board, 3, 0, 3, 'E')
  Battleship.place_ship(user_board, 4, 0, 2, 'E')
  
if __name__ == '__main__':
  run()







  






class Battleship(object):

  def place_ship(self, board, coordinate_x, coordinate_y, length, direction):
    for i in range(length):
        if direction == "N":
            el = (coordinate_x[0], coordinate_y[1] - i)
            board.add_ship(el)
        elif direction == "S":
            el = (coordinate_x[0], coordinate_y[1] + i)
            board.add_ship(el)
        elif direction == "W":
            el = (coordinate_x[0] - i, coordinate_y[1])
            board.add_ship(el)
        elif direction == "E":
            el = (coordinate_x[0] + i, coordinate_y[1])
            board.add_ship(el)
        else:
            print("Wrong direction")
            return False

  def __init__(self, body, direction):
      self.body = body
      self.direction = direction
class board:
  def __init__(self, width, height):
      self.width = width
      self.height = height
      self.board = []
      for i in range(height):
          self.board.append([])
          for j in range(width):
              self.board[i].append('~')
  def print_board(self):
      for i in range(self.height):
          print(self.board[i])
  

        
class Player:
  def __init__(self, name, board):
      self.name = name
      self.board = board

def run():
  user_board = board(8, 8)
  user = Player("user", user_board)
  computer = Player("Computer",(8, 8))
  #place battleships
  Battleship.place_ship(user_board, 0, 0, 5, 'E')
  Battleship.place_ship(user_board, 0, -1, 4, 'E')
  Battleship.place_ship(user_board, 0, -2, 3, 'E')
  Battleship.place_ship(user_board, 0, -3, 3, 'E')
  Battleship.place_ship(user_board, 0, -4, 2, 'E')

  
if __name__ == '__main__':
  run()







  






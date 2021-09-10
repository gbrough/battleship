class Battleship(object):
  @staticmethod
  def build(head, length, direction):
    body = []
    for i in range(length):
        if direction == "N":
            el = (head[0], head[1] - i)
        elif direction == "S":
            el = (head[0], head[1] + i)
        elif direction == "W":
            el = (head[0] - i, head[1])
        elif direction == "E":
            el = (head[0] + i, head[1])

        body.append(el)

    return Battleship(body, direction)
  
  def __init__(self, name, size, direction, head):
      self.name = name
      self.size = size
      self.direction = direction
  def get_ship_direction(self):
    if self.direction == 'h':
      return 'horizontal'
    else:
      return 'vertical'
  def get_ship_name(self):
      return self.name
  def get_ship_size(self):
      return self.size
class board:
  def __init__(self, player, width, height):
      self.width = width
      self.height = height
      self.player = player
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
  battleships = [
      Battleship("Aircraft Carrier", 5, 'h'),
      Battleship("Battleship", 4, 'h'),
      Battleship("Submarine", 3, 'h'),
      Battleship("Destroyer", 3, 'h'),
      Battleship("Patrol Boat", 2, 'h')
  ]
  print(battleships)
  #create players and boards
  user = Player("user", board(5, 5))
  computer = Player("Computer", board(5, 5))
  #place user battle ships
  
  print(battleships)
  
if __name__ == '__main__':
  run()







  






class Battleship(object):
  def __init__(self, name, size, direction):
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
      Battleship("Aircraft Carrier", 5),
      Battleship("Battleship", 4),
      Battleship("Submarine", 3),
      Battleship("Destroyer", 3),
      Battleship("Patrol Boat", 2)
  ]
  print(battleships)
  #create players and boards
  user = Player("Player 1", board(5, 5))
  computer = Player("Computer", board(5, 5))
  #place user battle ships
  b1 = battleships[0]
  

  

 

if __name__ == '__main__':
  run()







  






class Battleship:
  def __init__(self, name, size, location):
      self.name = name
      self.size = size
      self.location = location
  def get_ship_name(self):
      return self.name
  def get_ship_size(self):
      return self.size
  def get_ship_location(self):
      return self.location

class board:
  def __init__(self, battleship, width, height):
      self.battleship = battleship
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
  battleships = [
      Battleship("Aircraft Carrier", 5, [0,0]),
      Battleship("Battleship", 4, [0,1]),
      Battleship("Submarine", 3, [0,2]),
      Battleship("Destroyer", 3, [0,3]),
      Battleship("Patrol Boat", 2, [0,4])
  ]
  #create players
  user = Player("user", board(battleships[0], 5, 5))
  computer = Player("computer", board(battleships[0], 5, 5))
  #place ships
  user.board.battleship.location = [0,0]
  computer.board.battleship.location = [0,0]
  #print board
  user.board.print_board()
  computer.board.print_board()

if __name__ == '__main__':
  run()







  






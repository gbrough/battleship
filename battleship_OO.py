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

  def __init__(self, body, direction):
      self.body = body
      self.direction = direction
      self.hits = [False] * len(body)
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
  
  def place_ship(self, ship, head, direction):
      if direction == "N":
          for i in range(ship.length):
              self.board[head[0] - i][head[1]] = 'S'
      elif direction == "S":
          for i in range(ship.length):
              self.board[head[0] + i][head[1]] = 'S'
      elif direction == "W":
          for i in range(ship.length):
              self.board[head[0]][head[1] - i] = 'S'
      elif direction == "E":
          for i in range(ship.length):
              self.board[head[0]][head[1] + i] = 'S'
    
    
        
class Player:
  def __init__(self, name, board):
      self.name = name
      self.board = board

def run():
  battleships = [
      Battleship.build((0, 0), 2, 'E'),
      Battleship.build((1, 0), 3, 'E'),
      Battleship.build((2, 0), 3, 'E'),
      Battleship.build((3, 0), 4, 'E'),
      Battleship.build((4, 0), 5, 'E')
        ]
  print(battleships)
  #create players and boards
  user = Player("user", (5, 5))
  computer = Player("Computer",(5, 5))
  #place battleships on boards
  for ship in battleships:
      user.board.place_ship(ship)
      computer.board.place_ship(ship)
  #print boards
  user.board.print_board()
  computer.board.print_board()

  
  print(battleships)
  
if __name__ == '__main__':
  run()







  






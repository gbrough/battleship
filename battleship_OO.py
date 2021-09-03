class Battleship:
  def __init__(self, name, size, location):
      self.name = name
      self.size = size
      self.location = location
      self.hit = False
      self.sunk = False
      self.ships = []
      self.ships.append(Battleship("Aircraft Carrier", 5, [1, 1]))
      self.ships.append(Battleship("Battleship", 4, [1, 2]))
      self.ships.append(Battleship("Submarine", 3, [1, 3]))
      self.ships.append(Battleship("Destroyer", 3, [1, 4]))
      self.ships.append(Battleship("Patrol Boat", 2, [1, 5]))
  def hit_ship(self):
      self.hit = True
      return self.hit
  def sunk_ship(self):
      self.sunk = True
      return self.sunk
  def get_ship_type(self):
      return self.ship_type
  def get_ship_size(self):
      return self.ship_size
  def get_ship_location(self):
      return self.location
  def get_ship_name(self):
      return self.name

class board:
  def __init__(self, size):
      self.size = size
      self.board = []
      for i in range(size):
          self.board.append(["O"] * size)
  def print_board(self):
      for row in self.board:
          print(" ".join(row))
  def get_board(self):
      return self.board

class Player:
  def __init__(self, name, board):
      self.name = name
      self.board = board

if __name__ == '__main__':
  #create instance of players
  player1 = Player("Player", "board")
  computer = Player("Computer", "board")
  print(player1.name)
  print(computer.name)

  






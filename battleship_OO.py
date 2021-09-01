from random import randint

#battleship board class
class Board:
  def __init__(self, size):
    self.size = size
    self.board = []
    for i in range(size):
      self.board.append([" "] * size)
  def print_board(self):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in self.board:
      print("%d|%s|" % (row_number, "|".join(row)))
      row_number += 1

#player class
class Player:
  def __init__(self, name):
    self.name = name
    self.ships = []
  def place_ship(self, ship):
    self.ships.append(ship)

#ship class
class Ship:
  def __init__(self, name, size, row, col):
    self.name = name
    self.size = size
    self.row = row
    self.col = col
    self.hit = False

#battleship game class
class Game:
  def __init__(self, size):
    self.size = size
    self.board = Board(size)
    self.ship_sizes = [5, 4, 3, 3, 2]
    self.ships = []
    self.guess_board = []
    self.hit_count = 0
    self.miss_count = 0
    self.ship_count = 0
    self.ship_hit_count = []
    self.ship_miss_count = []
    for ship_size in self.ship_sizes:
      self.ships.append(Ship(ship_size))
    self.place_ships()
  def place_ships(self):
    for ship in self.ships:
      while True:
        x = randint(0, self.size - 1)
        y = randint(0, self.size - 1)
        if self.board.board[x][y] == " ":
          self.board.board[x][y] = ship.symbol
          self.board.print_board()
          break
  def guess(self, x, y):
    if self.board.board[x][y] == " ":
      self.board.board[x][y] = "X"
      self.guess_board[x][y] = "X"
      self.miss_count += 1
      return False
    else:
      self.board.board[x][y] = "X"
      self.guess_board[x][y] = "X"
      self.hit_count += 1
      return True
  def check_win(self):
    for ship in self.ships:
      if ship.hit_count == ship.size:
        return True
    return False
  def check_loss(self):
    if self.miss_count == 5:
      return True
    return False
  def check_ship_loss(self, ship):
    if ship.miss_count == ship.size:
      return True
    return False
  def check_ship_win(self, ship):
    if ship.hit_count == ship.size:
      return True
    return False
  def check_all_ships_sunk(self):
    for ship in self.ships:
      if not self.check_ship_loss(ship):
        return False
    return True
  def check_all_ships_hit(self):
    for ship in self.ships:
      if not self.check_ship_win(ship):
        return False
    return True

#create instance of boards
battleship_board = Board(8)
battleship_guess_board = Board(8)

#create instance of players
battleship_player = Player("Player 1")
battleship_ai = Player("Player 2")

#create instance of game
battleship_game = Game(8)





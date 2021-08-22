import random

class Game():
    registry = []
    moves = []

    def __init__(self):
        self.get_players()

    def get_players(self):
        for i in range(2):
            name = input("input name> ")
            player = Player(name)
            player.board = Board(name)
            player.board.grid = self.get_board(player)
            player.board.ships = self.get_ships()
            print("setting ships for", player.name)
            self.set_ships(player.board)
            self.registry.append(player)
        print("now, time to play!")
        self.play(self.registry)  # TODO <-----------
            
    def get_board(self, player):
        grid = []
        tile_num = 0
        width = player.board.WIDTH
        height = player.board.HEIGHT
        for y in range(width+1):
            for x in range(height+1):
                tile = Tile(tile_num, x, y)
                if (tile_num < width+1) or (x % width == 0) or (y % height == 0):
                    tile.is_border = True
                grid.append(tile)
                tile_num += 1
        return grid

    def get_ships(self):
        ships = [Ship(5, "Aircraft carrier"),
                 Ship(4, "Battleship"),
                 Ship(3, "Submarine"),
                 Ship(3, "Cruiser"),
                 Ship(2, "Patrol boat")]
        return ships

    def set_ships(self, board):
        for i in range(len(board.ships)):
            Helper().set_ships(board.ships[i], board.grid)

    def play(self, player):
        x = input("row> ")
        y = input("column> ")
        Helper().tile_check(player, x, y)
        exit()
        

class Player(object):
    def __init__(self, name):
        Game.registry.append(self)
        self.name = name
        self.board = []

class Board(object):
    def __init__(self, owner):
        self.owner = owner
        print("Hello {}, I'm creating your board".format(self.owner))
        self.grid = []
        self.ships = []
        self.WIDTH = 11
        self.HEIGHT = 11
        

class Ship(object):
    def __init__(self, length, name):
        self.length = length
        self.name = name
        self.sunk = False
        self.loc = []
        
        
class Tile(object):
    def __init__(self, number, row, column):
        self.number = number
        self.row = row
        self.column = column
        self.is_border = False
        self.has_ship = False
        self.bombed = False
        self.current_ship = "nothing but the deep blue sea here"


class Helper(object):
    def set_ships(self, ship, grid):
        node = random.randint(1, len(grid)-1)
        ship_length = ship.length
        horizontal = random.randint(0, 1)
        #check horizontal
        if horizontal:
            for i in range(ship_length):
                if grid[node + i].is_border or grid[node + i].has_ship:
                    self.set_ships(ship, grid)
                    break
            else:
                for i in range(ship_length):
                    grid[node + i].has_ship = True
                    grid[node + i].current_ship = ship.name
                    ship.loc.append(grid[node + i])
                print("your", ship.name, "placed")
        else:
        #check vertical
            for i in range(ship_length):
                if grid[node + (i*11)].is_border or grid[node + (i*11)].has_ship:
                    self.set_ships(ship, grid)
                    break
            else:
                for i in range(ship_length):
                    grid[node + (i*12)].has_ship = True
                    grid[node + (i*12)].current_ship = ship.name
                    ship.loc.append(grid[node + (i*12)])
                print("your", ship.name, "placed")

    def tile_check(self, player, x, y): # TODO <----------
        print(player)
        exit()

battleship = Game()
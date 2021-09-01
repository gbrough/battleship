
#battleship class
class battleship:
    def __init__(self, name, size, x, y):
        self.name = name
        self.size = size
        self.x = x
        self.y = y
        self.hit = 0
        self.miss = 0
        self.sunk = False
        self.ship_type = 'battleship'
        self.ship_size = 5

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        
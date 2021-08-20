
class BattleShip:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.status = "available"
    def __str__(self):
        return 'The {} ship takes {} hits to sink'.format(self.name, self.size)
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status = status

carrier = BattleShip('carrier', 5)
submarine = BattleShip('submarine', 3)
destroyer = BattleShip('destroyer', 2)

print(carrier, carrier.get_status())
carrier.set_status('sunk')
print(carrier, carrier.get_status())

# dictionary to hold ship location
ships = {'carrier': carrier, 'submarine': submarine, 'destroyer':destroyer}






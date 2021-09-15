import copy
import random
import time

class GameBoard(object):

    def __init__(self, battleships, width, height):
        self.battleships = battleships
        self.shots = []
        self.width = width
        self.height = height

    # * Update battleship with any hits
    # * Save the fact that the shot was a 
    # hit or a miss
    #
    # If hit, returns the hit battleship
    # Else returns None
    def take_shot(self, shot_location):
        hit_battleship = None
        is_hit = False
        for b in self.battleships:
            idx = b.body_index(shot_location)
            if idx is not None:
                is_hit = True
                b.hits[idx] = True
                hit_battleship = b
                break

        self.shots.append(Shot(shot_location, is_hit))
        return hit_battleship

    def is_game_over(self):
        return all([b.is_destroyed() for b in self.battleships])


class Shot(object):

    def __init__(self, location, is_hit):
        self.location = location
        self.is_hit = is_hit

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

    def body_index(self, location):
        try:
            return self.body.index(location)
        except ValueError:
            return None

    def is_destroyed(self):
        return all(self.hits)

class Player(object):

    def __init__(self, name, shot_f):
        self.name = name
        self.shot_f = shot_f

def render_basic(game_board, show_battleships=False):
    header = "+" + "-" * game_board.width + "+"
    print(header)

    # Construct empty board
    board = []
    for _ in range(game_board.width):
        board.append([None for _ in range(game_board.height)])

    if show_battleships:
        # Add the battleships to the board
        for b in game_board.battleships:
            for i, (x, y) in enumerate(b.body):
                if b.direction == "N":
                    chs = ("v", "|", "^")
                elif b.direction == "S":
                    chs = ("^", "|", "v")
                elif b.direction == "W":
                    chs = (">", "=", "<")
                elif b.direction == "E":
                    chs = ("<", "=", ">")
                else:
                    raise "Unknown direction"

                if i == 0:
                    ch = chs[0]
                elif i == len(b.body) - 1:
                    ch = chs[2]
                else:
                    ch = chs[1]
                board[x][y] = ch

    # Add the shots to the board
    for sh in game_board.shots:
        x, y = sh.location
        if sh.is_hit:
            ch = "X"
        else:
            ch = "@"
        board[x][y] = ch

    for y in range(game_board.height):
        row = []
        for x in range(game_board.width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")

    print(header)

# type, metadata (player,...)
def announce_en(event_type, metadata={}):
    if event_type == "game_over":
        print("%s WINS THE GAME!" % metadata['player'])
    elif event_type == "new_turn":
        print("%s YOUR TURN!" % metadata['player'])
    elif event_type == "miss":
        print("%s MISSED!" % metadata['player'])
    elif event_type == "battleship_destroyed":
        print("%s DESTROYED a battleship!" % metadata['player'])
    elif event_type == "battleship_hit":
        print("%s HIT a battleship!" % metadata['player'])
    else:
        print("UNKNOWN EVENT TYPE: %s" % event_type)


def announce_none(event_type, metadata={}):
    pass


def get_random_ai_shot(game_board):
    x = random.randint(0, game_board.width - 1)
    y = random.randint(0, game_board.height - 1)
    return (x, y)


def random_sleepy_ai(sleep_time):
    return sleepy_ai(get_random_ai_shot, sleep_time)


def sleepy_ai(ai_f, sleep_time):
    def f(game_board):
        time.sleep(sleep_time)
        return ai_f(game_board)
    return f


def get_clever_ai(game_board):
    return (0, 0)


def get_human_shot(game_board):
    inp = input("Where do you want to shoot?\n")
    # TODO: deal with invalid input
    xstr, ystr = inp.split(",")
    x = int(xstr)
    y = int(ystr)

    return (x, y)


def run(announce_f, render_f):
    battleships = [
        Battleship.build((1,1), 2, "N"),
        Battleship.build((5,8), 5, "N"),
        Battleship.build((2,3), 4, "E"),
        Battleship.build((6,6), 3, "S"),
        Battleship.build((9,9), 5, "W"),
    ]

    # https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
    game_boards = [
        GameBoard(battleships, 10, 10),
        GameBoard(copy.deepcopy(battleships), 10, 10)
    ]

    players = [
        Player("Rob", random_sleepy_ai(1)),
        Player("Alice", random_sleepy_ai(1)),
    ]

    offensive_idx = 0
    while True:
        # defensive player is the non-offensive one
        defensive_idx = (offensive_idx + 1) % 2

        defensive_board = game_boards[defensive_idx]
        offensive_player = players[offensive_idx]

        announce_f("new_turn", {"player": offensive_player.name})
        shot_location = offensive_player.shot_f(defensive_board)

        hit_battleship = defensive_board.take_shot(shot_location)
        if hit_battleship is None:
            announce_f("miss", {"player": offensive_player.name})
        else:
            if hit_battleship.is_destroyed():
                announce_f("battleship_destroyed", {"player": offensive_player.name})
            else:
                announce_f("battleship_hit", {"player": offensive_player.name})

        render_f(defensive_board)

        if defensive_board.is_game_over():
            announce_f("game_over", {"player": offensive_player.name})
            break

        # offensive player becomes the previous defensive
        # player
        offensive_idx = defensive_idx

if __name__ == "__main__":
    run(announce_en, render_basic)
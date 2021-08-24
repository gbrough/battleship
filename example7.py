"""Hackbright Battleship!

This is an object-oriented version of Battleship. It's a good demonstration
of class-based game design.

The Game class represents a game and holds the state of the game
(player1, player2, and the current player.

The Player class represents an individual player. It holds information about
their name, board, and ships. It also has a link to the other player ("opponent"),
which makes it easy to find the other player.

The ships are all subclasses of the Ship class, which handles logic around
knowing when a ship is sunk, how to place a ship on the board, etc.

Joel Burton <joel@joelburton.com>
"""

import random
import sys


# If set to true, print board without so much spacing
# On bigger screens, you can set this to False
TIGHT = True

# Colors
#
# You can safely ignore this. These functions print out a message
# in a console color if the console appears to be a live TTY (that is, not
# being piped out/in a test/etc.)

NO_COLOR = False  # If the colors annoy you, set this to True

WATER = lambda msg: ('\033[34m%s\033[0m' % msg
                     if sys.stdout.isatty() and not NO_COLOR else msg)
SUNK = lambda msg: ('\033[91m%s\033[0m' % msg
                    if sys.stdout.isatty() and not NO_COLOR else msg)
HIT = lambda msg: ('\033[31m%s\033[0m' % msg
                   if sys.stdout.isatty() and not NO_COLOR else msg)


#####################################################################################


class Ship(object):
    """Type of ship."""

    _length = 0  # length of ship
    name = ""  # name of ship
    coords = []  # list of (col, row) coordinates this ship occupies

    def __init__(self):
        assert self._length > 0 and self.name, "Must subclass with length and name!"

        self.hits = 0
        self.coords = []

    def is_sunk(self):
        """Is this ship sunk?"""

        return self.hits == self._length

    def place(self, col, row, direction):
        """Place ship.

        Given a row and column and direction, determine coordinates
        ship will occupy and update it's coordinates property.

        Raises an exception for an illegal direction.

        This is meant to be an abstract class--you should subclass it
        for individual ship types.

            >>> class TestShip(Ship):
            ...     _length = 3
            ...     name = "Test Ship"

        Let's make a ship and place it:

            >>> ship = TestShip()

            >>> ship.place(1, 2, "H")
            >>> ship.coords
            [(1, 2), (2, 2), (3, 2)]

            >>> ship.place(1, 2, "V")
            >>> ship.coords
            [(1, 2), (1, 3), (1, 4)]

        Illegal directions raise an error:

            >>> ship.place(1, 2, "Z")
            Traceback (most recent call last):
            ...
            ValueError: Illegal direction
        """


class AircraftCarrier(Ship):
    _length = 5
    name = "Aircraft Carrier"


class Destroyer(Ship):
    _length = 2
    name = "Destroyer"


class Submarine(Ship):
    _length = 3
    name = "Submarine"


class Battleship(Ship):
    _length = 4
    name = "Battleship"
 

# List of ship types, in the order player should place them
SHIP_TYPES = [AircraftCarrier, Battleship, Submarine, Destroyer]


class Player(object):
    """Object for a player.

    Players have a board with their ships/opponent's moves, their ships,
    their name, and a link to their opponent.
    """

    name = ""  # will be name for player
    opponent = None  # will be the opponent object for this player

    # These attributes are private -- other classes shouldn't
    # need to inspect or change them directly. It's smart to note
    # which attributes/methods are private, so it's more clear for others
    # how to use your class. In this case, this says clearly that
    # the other classes shouldn't mess with this stuff.

    _board = None  # will be 10x10 matrix (list-of-lists) for board
    _ships = None  # will be list of living ships for user

    def __init__(self, name):
        """Create player:

        - set up their board
        - set up their (empty initially) list of ships

        Let's create a player:

            >>> player = Player('Jane')

        They should have an empty board:

            >>> player._board   # doctest: +NORMALIZE_WHITESPACE
            [[False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False, False, False]]

        THey should have no ships:

            >>> player._ships
            []

        They should have no opponent (yet!):

            >>> player.opponent is None
            True

        """

        self.name = name

        self._board = []
        for row in range(10):
            self._board.append([False] * 10)

        self._ships = []

    def place_ship(self, ship, col, row, direction):
        """Place a ship on the board at col, row, going in direction.

        :col: 0-based column
        :row: 0-based row
        :direction: "H" or "V"

        LEt's create a player and place a ship:

            >>> player = Player('Jane')
            >>> destroyer = Destroyer()
            >>> player.place_ship(destroyer, 1, 2, "V")

        Did it place the destroyer on all the cells for it?

            >>> player._board[1][2] is destroyer
            True
            >>> player._board[1][3] is destroyer
            True

        Did it get the coordinates right?

            >>> destroyer.coords
            [(1, 2), (1, 3)]

        Is the destroyer the only ship in their player's arsenal?

            >>> player._ships == [destroyer]
            True
        """

        # Have ship determine it's own coordinates
        ship.place(col, row, direction)

        for col, row in ship.coords:
            # For each coord ship occupies, put it on board

            if self._board[col][row]:
                raise ValueError("Already a ship there")

            else:
                self._board[col][row] = ship

        # Add it to the player's arsenal
        self._ships.append(ship)

    def place_ships(self):
        """Prompt a player to place their ships."""

        for ship in SHIP_TYPES:
            # Prompt the player for each type of ship

            while True:
                # Keep looping until a legal placement is made

                try:
                    place = raw_input(
                        "\nPlace your %s (col row H/V, eg '00H') >" % ship.name)
                    col = int(place[0])
                    row = int(place[1])
                    direction = place[2].upper()
                    self.place_ship(ship(), col, row, direction)
                    print()
                    self.show_board(show_hidden=True)

                    # A legal placement was made, so we can break
                    break

                except (IndexError, ValueError) as e:
                    print("\n(%s: try again)" % e)

        print("\nDone!\n")

    def show_board(self, show_hidden=False, tight=TIGHT):
        """Print out board:

        _ = missed here
        * = hit here
        # = destroyed ship here
        . = nothing here
        ELSE = first letter of ship type hidden here

        If `show_hidden` is False, hidden ships are shown as nothing-here.
        This is the view shown to opponents.

        If `tight` is True, skip some of the space in the board
        (good for tests and smaller screens)

        So we can see this, let's create a player and make a few
        shots:

            >>> player = Player('Jane')
            >>> destroyer = Destroyer()
            >>> player._board[1][2] = destroyer
            >>> player._board[1][3] = destroyer
            >>> player._board[0][0] = "_"  # miss
            >>> player._board[1][2] = "*"  # hit

        Here's what the opponent should see:

            >>> player.show_board(tight=True)  # doctest: +NORMALIZE_WHITESPACE
              0 1 2 3 4 5 6 7 8 9
            0 _ . . . . . . . . .
            1 . . . . . . . . . .
            2 . * . . . . . . . .
            3 . . . . . . . . . .
            4 . . . . . . . . . .
            5 . . . . . . . . . .
            6 . . . . . . . . . .
            7 . . . . . . . . . .
            8 . . . . . . . . . .
            9 . . . . . . . . . .

        The player can see their own ships:

            >>> player.show_board(show_hidden=True, tight=True
            ...     ) # doctest: +NORMALIZE_WHITESPACE
              0 1 2 3 4 5 6 7 8 9
            0 _ . . . . . . . . .
            1 . . . . . . . . . .
            2 . * . . . . . . . .
            3 . D . . . . . . . .
            4 . . . . . . . . . .
            5 . . . . . . . . . .
            6 . . . . . . . . . .
            7 . . . . . . . . . .
            8 . . . . . . . . . .
            9 . . . . . . . . . .

        """

        # Print col numbers across top
        if tight:
            print(" ", end=' ')
            for coli in range(10):
                print("%s" % coli, end=' ')
            print()
        else:
            print("  ", end=' ')
            for coli in range(10):
                print("%s  " % coli, end=' ')
            print("\n")

        for rowi in range(10):

            # Print row numbers across left
            print(rowi, end=' ')
            if not tight:
                print("", end=' ')

            # Print cells
            for coli in range(10):
                ship = self._board[coli][rowi]

                if ship == "*":
                    print(HIT("*"), end=' ')

                elif ship == "#":
                    print(SUNK("#"), end=' ')

                elif ship == "_":
                    print(WATER("_"), end=' ')

                elif not ship or not show_hidden:
                    # Square is empty OR is enemy ship & you can't see it yet
                    print(WATER("."), end=' ')

                else:
                    # Cell has ship and you're allowed to see it
                    print("%s" % ship.name[0], end=' ')

                if not tight:
                    print(" ", end=' ')  # add a space

            print("" if tight else "\n")

    def handle_shot(self, col, row):
        """Handle being shot at at col, row.

        If the shot is in an already-tried spot:
        - raise ValueError("You've already played there")

        If the shot misses:
         - update the board to show '_' for that cell

        Else, If the shot hits a ship:
        - update the board to '*' for that cell
        - update the ship's hits
        - check to see if it's destroyed
        - report a hit

        If the shot destroys a ship:
        - update ALL the ship's coordinates to '#'
        - report the sunk ship

        Let's create a player and add a ship:

            >>> player = Player('Jane')
            >>> destroyer = Destroyer()
            >>> player._board[1][2] = destroyer
            >>> player._board[1][3] = destroyer

        Handle misses:

            >>> player.handle_shot(0, 0)
            Miss

            >>> player.handle_shot(0, 0)
            Traceback (most recent call last):
            ...
            ValueError: You've already played there

        Handle hits:

            >>> player.handle_shot(1, 2)
            Hit!

            >>> player.handle_shot(1, 2)
            Traceback (most recent call last):
            ...
            ValueError: You've already played there


        Handle sinking things:

            >>> player.handle_shot(1, 3)
            Hit!
            You sunk my Destroyer
        """

        ship = self._board[col][row]

        if not ship:
            self._board[col][row] = "_"
            print("Miss")

        elif isinstance(ship, Ship):
            # Hit a real ship (anything subclassing Ship)
            ship.hits += 1
            print(HIT("Hit!"))
            self._board[col][row] = "*"

            if ship.is_sunk():
                for col, row in ship.coords:
                    self._board[col][row] = "#"
                print(SUNK("You sunk my " + ship.name))

        else:
            raise ValueError("You've already played there")

    def is_dead(self):
        """Is player dead (out of ships)?

            >>> player = Player('Jane')

        Since they have no placed ships, they're technically dead:

            >>> player.is_dead()
            True

        Let's place some ships:

            >>> destroyer = Destroyer()
            >>> player.place_ship(destroyer, 1, 2, "V")
            >>> player.is_dead()
            False

        And we'll hit a ship:

            >>> player.handle_shot(1, 2)
            Hit!

            >>> player.is_dead()
            False

        And destroy it (and it's their only ship, too1)

            >>> player.handle_shot(1, 3)
            Hit!
            You sunk my Destroyer

            >>> player.is_dead()
            True
        """


class Game(object):
    """Battleship game."""

    player1 = None
    player2 = None
    player = None  # current player

    def __init__(self, player1_name, player2_name):
        """Create game.

        Create players, assign each other as opponents, and pick a start player.
        """

        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

        self.player1.opponent = self.player2
        self.player2.opponent = self.player1

    def pick_start_player(self):
        """Pick a starting player randomly."""

        self.player = random.choice([self.player1, self.player2])

    def setup_ships(self):
        """Prompt both players to place their ships."""

        for i in range(2):
            print("=" * 60)
            print("%s: Place your ships (%s, turn away!)" % (
                self.player.name, self.player.opponent.name))
            self.player.place_ships()
            raw_input("\nPress ENTER to switch players >")
            print("\n" * 80)  # scroll private stuff off screen
            self.player = self.player.opponent

    def play(self):
        """Main game loop.

        Keep playing until a player has lost all their ships.

        - show the player their private board
        - show the player their opponent's non-secret board
        - prompt for a move
        - the opponent handles the player's move
        """

        while True:
            # Loop until someone wins

            print()
            print("=" * 40)
            print("\n%s, let's attack %s\n" % (
                self.player.name, self.player.opponent.name))
            self.player.opponent.show_board()

            while True:
                # Loop until a valid move is made

                try:
                    move = raw_input("\nMove (col row, e.g. '00') >")
                    col = int(move[0])
                    row = int(move[1])
                    print()
                    self.player.opponent.handle_shot(col, row)

                    # Valid move was made, so we can break out
                    break

                except (ValueError, IndexError) as e:
                    print("\n(%s: try again)" % e)

            print()
            self.player.opponent.show_board()

            if self.player.opponent.is_dead():
                break

            self.player = self.player.opponent

        print("\n *** YOU WIN!")


def play(player1_name, player2_name):
    """PLay battleship!

    This creates a game, picks a start player, prompts the players for
    setup, and shows the instructions. It then enters the main
    game loop.
    """

    game = Game(player1_name, player2_name)
    game.pick_start_player()

    print(HIT("\n\n*** HACKBRIGHT BATTLESHIP: %s vs %s ***" % (
        game.player.name, game.player.opponent.name)))

    print("""
Battleship is played on a 10x10 grid. Each player has a separate,
secret board. Your goal is to sink your opponent's ships before
she sinks yours.

Each player will place their four ships secretly. To place a ship,
you'll be prompted for a location. Enter it like '12H', where that is
the column=1, the row=2, and going horizontally ("V" for vertically).

""")
    game.setup_ships()

    print("""
How, play begins. On your turn, you'll be shown your opponent's board.
Enter coordinates for an attack on your opponent. Enter it like "12",
where column=1 and row=2.

You will receive a report on whether you missed, hit a ship, or
sunk a ship.
""")
    game.play()

    print("""
That was fun! Let's play again soon!
""")


if __name__ == '__main__':
    import doctest

    # When called, this always runs its tests
    mod_fail = doctest.testmod().failed
    story_fail = doctest.testfile('battleship.txt',
                                  optionflags=doctest.NORMALIZE_WHITESPACE).failed
    if mod_fail + story_fail == 0:
        print("\n*** ALL TEST PASSED. AMAZING!\n")

        # If you run this with two arguments, it also starts an interactive game
        #
        # for example:
        #
        #   python battleship.py Balloonicorn Joel

        if len(sys.argv) == 3:
            play(sys.argv[1], sys.argv[2])
Read and understand the tests, including the docfile test in battleship.txt.

Battleship Test
===============

Let's make a player::

    >>> from battleship import Player
    >>> jane = Player('Jane')

Let's add some ships for her::

    >>> from battleship import Destroyer, AircraftCarrier, Submarine, Battleship
    >>> jane.place_ship(Destroyer(), 0, 0, "H")
    >>> jane.place_ship(AircraftCarrier(), 1, 1, "H")
    >>> jane.place_ship(Submarine(), 6, 6, "V")
    >>> jane.place_ship(Battleship(), 3, 3, "V")

Let's look at the board with the ships on it::

    >>> jane.show_board(show_hidden=True, tight=True)
      0 1 2 3 4 5 6 7 8 9
    0 D D . . . . . . . .
    1 . A A A A A . . . .
    2 . . . . . . . . . .
    3 . . . B . . . . . .
    4 . . . B . . . . . .
    5 . . . B . . . . . .
    6 . . . B . . S . . .
    7 . . . . . . S . . .
    8 . . . . . . S . . .
    9 . . . . . . . . . .


Her opponent shoots at her a few times and misses::

    >>> jane.handle_shot(8, 8)
    Miss

    >>> jane.handle_shot(7, 7)
    Miss

Here's how her opponent would see the board::

    >>> jane.show_board(tight=True)
      0 1 2 3 4 5 6 7 8 9
    0 . . . . . . . . . .
    1 . . . . . . . . . .
    2 . . . . . . . . . .
    3 . . . . . . . . . .
    4 . . . . . . . . . .
    5 . . . . . . . . . .
    6 . . . . . . . . . .
    7 . . . . . . . _ . .
    8 . . . . . . . . _ .
    9 . . . . . . . . . .

Oh no!::

    >>> jane.handle_shot(0, 0)
    Hit!

    >>> jane.show_board(tight=True)
      0 1 2 3 4 5 6 7 8 9
    0 * . . . . . . . . .
    1 . . . . . . . . . .
    2 . . . . . . . . . .
    3 . . . . . . . . . .
    4 . . . . . . . . . .
    5 . . . . . . . . . .
    6 . . . . . . . . . .
    7 . . . . . . . _ . .
    8 . . . . . . . . _ .
    9 . . . . . . . . . .

    >>> jane.handle_shot(1, 0)
    Hit!
    You sunk my Destroyer

    >>> jane.show_board(tight=True)
      0 1 2 3 4 5 6 7 8 9
    0 # # . . . . . . . .
    1 . . . . . . . . . .
    2 . . . . . . . . . .
    3 . . . . . . . . . .
    4 . . . . . . . . . .
    5 . . . . . . . . . .
    6 . . . . . . . . . .
    7 . . . . . . . _ . .
    8 . . . . . . . . _ .
    9 . . . . . . . . . .


And, of course, it should tell her opponent when they repeat actions:

    >>> jane.handle_shot(0, 0)
    Traceback (most recent call last):
    ...
    ValueError: You've already played there

    >>> jane.handle_shot(8, 8)
    Traceback (most recent call last):
    ...
    ValueError: You've already played there

Since Jane has some ships left, she hasn't lost::

    >>> jane.is_dead()
    False
There are two unimplemented methods:

The Ship.place method:

class Ship(object):  # ...
    def place(self, col, row, direction):
        """Place ship.

        Given a row and column and direction, determine coordinates
        ship will occupy and update it's coordinates property.

        Raises an exception for an illegal direction.

        This is meant to be an abstract class--you should subclass it
        for individual ship types.

            >>> class TestShip(Ship):
            ...     _length = 3
            ...     name = "Test Ship"

        Let's make a ship and place it:

            >>> ship = TestShip()

            >>> ship.place(1, 2, "H")
            >>> ship.coords
            [(1, 2), (2, 2), (3, 2)]

            >>> ship.place(1, 2, "V")
            >>> ship.coords
            [(1, 2), (1, 3), (1, 4)]

        Illegal directions raise an error:

            >>> ship.place(1, 2, "Z")
            Traceback (most recent call last):
            ...
            ValueError: Illegal direction
        """ 
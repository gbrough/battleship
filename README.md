Fixes
 - Add row and column headers to the table.
 - Change starting column from 0 to 1.


1 player game. Player guesses location of 5 ships, limit of 10 tries
  - 64 total spaces, 17 occupied, 47 empty

define&print board
create vertical and horizontal coordinates
  - empty spaces 
  - O's for miss
  - X's for hit
create manual ship
ship types
  -Carrier, which has five holes
  -Battleship, which has four holes
  -Cruiser, which has three holes
  -Submarine, which has three holes
  -Destroyer, which has two holes


Additional Games: 
1. 2 Player game - 2 players take turns shooting at each other
2. Player plays against computer with a random guesses
3. Improve AI

Feature considerations
 - Add classes and objects
 - Base class ship
 - Derived class for each type of ship
 - Dictionary of ships and their location
 
from battleship_single_player import count_hit_ships, print_board
import unittest

class BattleshipTest(unittest.TestCase):

  def test_count_hit_ships_empty_board(self):
    board = [" " * 8 for x in range(8)]
    count = count_hit_ships(board)
    self.assertEqual(count, 0)

  def test_count_hit_ships_win_condition(self):
    board = [[" "] * 8 for x in range(8)]
    for i in range(6):
      board[0][i] = "X"
    print_board(board)
    count = count_hit_ships(board)
    self.assertGreater(count, 5)

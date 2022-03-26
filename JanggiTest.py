import unittest
from JanggiMain import JanggiGame

class UnitTests(unittest.TestCase):
    test_game = JanggiGame()
    test_game._board.print_board()

    def test_starting_player_turn(self):
        # Blue starts
        test_game = JanggiGame()
        self.assertFalse(test_game.make_move("a4", "a5"))  # Red cannot move first
        self.assertTrue(test_game.make_move("a7", "a6"))  # Blue can move first

    def test_turn_taking(self):
        test_game = JanggiGame()
        self.assertEqual(test_game.get_player_turn(), "B")
        test_game.make_move("a7", "a6")
        self.assertEqual(test_game.get_player_turn(), "R")
        test_game.make_move("a4", "a5")
        self.assertEqual(test_game.get_player_turn(), "B")

    def test_player_pass_turn(self):
        test_game = JanggiGame()
        test_game.make_move("a7", "a7")  # Blue pass
        self.assertEqual(test_game.get_player_turn(), "R")
        self.assertTrue(test_game.make_move("a4", "a5"))  # Red moves

    def test_player_turn_incorrect_move(self):
        test_game = JanggiGame()
        test_game.make_move("a7", "a8")  # Blue incorrect move
        self.assertEqual(test_game.get_player_turn(), "B")

    def test_empty_location(self):
        test_game = JanggiGame()
        self.assertFalse(test_game.make_move("a6", "a7"))  # Blue incorrect move

    # Piece Movement
    def test_soldier_movement(self):
        """Verify solider movements are correct"""
        test_game = JanggiGame()

        # Basic Movements
        self.assertTrue(test_game.make_move("a7", "a6"))  # forward
        self.assertTrue(test_game.make_move("g4", "h4"))  # left
        self.assertTrue(test_game.make_move("a6", "b6"))  # right
        test_game.make_move("h4", "h4")  # pass
        self.assertFalse(test_game.make_move("b6", "b7"))  # backward
        test_game.make_move("b6", "b6")
        self.assertFalse(test_game.make_move("h4", "g5"))  # diagonal
        self.assertFalse(test_game.make_move("h4", "i5"))  # diagonal
        self.assertFalse(test_game.make_move("h4", "g3"))  # backwards diagonal
        self.assertFalse(test_game.make_move("h4", "i3"))  # backwards diagonal

        # Fortress movement
        test_game.make_move("c4", "c5")
        test_game.make_move("b6", "b6")
        test_game.make_move("c5", "c6")
        test_game.make_move("b6", "b6")
        test_game.make_move("c6", "c7")
        test_game.make_move("b6", "b6")
        test_game.make_move("c7", "c8")
        test_game.make_move("b6", "b6")
        test_game.make_move("c8", "d8")
        test_game.make_move("e9", "f9")
        self.assertTrue(test_game.make_move("d8", "e9"))  # diagonal soldier movement in fortress

    def test_general_movement(self):
        test_game = JanggiGame()
        self.assertTrue(test_game.make_move("e9", "e8"))  # forward
        self.assertTrue(test_game.make_move("e2", "e1")) # backward
        self.assertTrue(test_game.make_move("e8", "d8"))  # left
        test_game.make_move("e1", "e2")
        self.assertTrue(test_game.make_move("d8", "e8"))  # right
        self.assertTrue(test_game.make_move("e2", "d3"))

        test_game._board.print_board()

if __name__ == '__main__':
    unittest.main()
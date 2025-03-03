import unittest
from RPS import player

class TestRPS(unittest.TestCase):
    def test_player(self):
        """Ensures that the player function returns valid moves"""
        valid_moves = ["R", "P", "S"]
        self.assertIn(player("R"), valid_moves)
        self.assertIn(player("P"), valid_moves)
        self.assertIn(player("S"), valid_moves)
        self.assertIn(player(""), valid_moves)

if __name__ == "__main__":
    unittest.main()

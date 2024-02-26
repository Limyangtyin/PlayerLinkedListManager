import unittest
from player import Player

class MyTestCase(unittest.TestCase):
    def test_player_name(self):
        player = Player(1, "Josh")
        self.assertEqual(player.name, "Josh")  # add assertion here


    def test_player_id(self):
        player = Player(1, "Josh")
        self.assertEqual(player.uid, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()

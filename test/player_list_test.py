import unittest
from player_list import PlayerList
from player_node import PlayerNode
from player import Player
class MyTestCase(unittest.TestCase):
    def test_add_at_head_when_empty_list(self):
        player_list = PlayerList()
        self.assertEqual(player_list.is_empty(), True)  # check if the list is empty

        player_node = PlayerNode(Player(1, "Josh"))
        player_list.add_at_head(player_node)
        self.assertEqual(player_list.is_empty(), False)  # check if the list is not empty
        self.assertEqual(player_list._head, player_node)  # check if the head is player

    def test_add_at_head_when_is_not_empty_list(self):
        player_node = PlayerNode(Player(1, "Josh"))
        player_list = PlayerList(player_node)
        self.assertEqual(player_list.is_empty(), False)  # check if the list is not empty

        player_node2 = PlayerNode(Player(2, "Abby"))
        player_list.add_at_head(player_node2)
        self.assertEqual(player_list.is_empty(), False)  # check if the list is not empty
        self.assertEqual(player_list._head, player_node2)  # check if the head is player 2
        self.assertEqual(player_node2.next, player_node)  # check if the next player is player 1

if __name__ == '__main__':
    unittest.main()

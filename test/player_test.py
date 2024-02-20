import unittest
from player import Player
class MyTestCase(unittest.TestCase):
    def test_uid(self):
        uid = 1
        name = "Abby"
        comb = Player(uid, name)
        uid_result = comb.uid

        self.assertEqual(uid_result, uid, "uid value is incorrect")

    def test_name(self):
        uid = 1
        name = "Page"
        comb = Player(uid, name)
        name_result = comb.name

        self.assertEqual(name_result, name, "name value is incorrect")

if __name__ == '__main__':
    unittest.main()

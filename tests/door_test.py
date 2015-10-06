import unittest
from lib.door import Door

class DoorTest(unittest.TestCase):

    def test_open(self):
        door = Door('goat')
        self.assertEqual(True, door.is_open())

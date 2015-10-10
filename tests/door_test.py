import unittest
from lib.door import Door

class DoorTest(unittest.TestCase):

    def test_door_is_open_after_creation(self):
        door = Door('goat')
        self.assertEqual(False, door.is_open)

    def test_door_has_correct_prize_after_creation(self):
        door = Door('car')
        self.assertEqual('car', door.prize)

    def test_door_can_be_opened(self):
        door = Door('goat')
        door.open()
        self.assertEqual(True, door.is_open)

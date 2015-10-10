import unittest
from lib.door import Door

class DoorTest(unittest.TestCase):

    def test_door_is_open_after_creation(self):
        door = Door(False)
        self.assertEqual(False, door.is_open)

    def test_door_has_correct_prize_status_after_creation(self):
        door = Door(False)
        self.assertEqual(False, door.has_prize)

    def test_door_can_be_opened(self):
        door = Door(False)
        door.open()
        self.assertEqual(True, door.is_open)

    def test_calling_open_twice_doesnt_close_the_door(self):
        door = Door(False)
        door.open()
        door.open()
        self.assertEqual(True, door.is_open)

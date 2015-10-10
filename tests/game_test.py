import unittest
from lib.game import Game
from lib.door import Door

class GameTest(unittest.TestCase):

    def test_first_round(self):
        door_1, door_2, door_3 = Door(False), Door(False), Door(True)
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 0
        game.host_open_door()
        self.assertEqual(True, door_2.is_open)

    def test_different_first_round(self):
        door_1, door_2, door_3 = Door(False), Door(True), Door(False)
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 0
        game.host_open_door()
        self.assertEqual(True, door_3.is_open)

    def test_case_where_contestant_guesses_correctly(self):
        door_1, door_2, door_3 = Door(False), Door(True), Door(False)
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 1
        game.host_open_door()
        self.assertEqual(False, door_2.is_open)
        self.assertEqual(True, door_1.is_open ^ door_3.is_open)

    def test_contestant_can_switch(self):
        door_1, door_2, door_3 = Door(False), Door(True), Door(False)
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 0
        game.contestant_switch()
        self.assertNotEqual(0, game.contestant_guess)

    def test_correct_loss(self):
        door_1, door_2, door_3 = Door(False), Door(True), Door(False)
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 0
        self.assertEqual(False, game.contestant_has_won())

    def test_correct_win(self):
        door_1, door_2, door_3 = Door(False), Door(True), Door(False)
        game = Game(door_1, door_2, door_3)
        game.contestant_guess = 1
        self.assertEqual(True, game.contestant_has_won())

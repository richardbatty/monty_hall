import random

class Game():

    def __init__(self, door_1, door_2, door_3):
        self.doors = [door_1, door_2, door_3]
        self.contestant_guess = None

    def host_open_door(self):
        enumerated_doors = enumerate(self.doors)
        openable_doors = [door for i, door in enumerated_doors if self.is_openable(i, door)]
        return random.choice(openable_doors).open()

    def is_openable(self, door_number, door):
        return door_number != self.contestant_guess and door.prize != 'car'

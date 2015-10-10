import random

class Game():

    def __init__(self, door_1, door_2, door_3):
        self.doors = [door_1, door_2, door_3]
        self.contestant_guess = None

    def host_open_door(self):
        openable_doors = [door for door in self.doors if self.is_openable_by_host(door)]
        return random.choice(openable_doors).open()

    def contestant_switch(self):
        choosable_doors = [door for door in self.closed_doors() if door != self.contestant_guess]
        self.contestant_guess = random.choice(choosable_doors)

    def is_openable_by_host(self, door):
        return door != self.contestant_guess and not door.has_prize

    def closed_doors(self):
        return [door for door in self.doors if not door.is_open]

    def contestant_has_won(self):
        return self.contestant_guess.has_prize

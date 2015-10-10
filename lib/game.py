import random

class Game():

    def __init__(self, door_1, door_2, door_3):
        self.doors = [door_1, door_2, door_3]
        self.contestant_guess = None

    def host_open_door(self):
        enumerated_doors = enumerate(self.doors)
        openable_doors = [door for i, door in enumerated_doors if self.is_openable_by_host(i, door)]
        return random.choice(openable_doors).open()

    def contestant_switch(self):
        choosable_doors = [door_no for door_no in self.closed_doors() if door_no != self.contestant_guess]
        self.contestant_guess = random.choice(choosable_doors)

    def is_openable_by_host(self, door_number, door):
        return door_number != self.contestant_guess and not door.has_prize

    def closed_doors(self):
        enumerated_doors = enumerate(self.doors)
        return [i for i, door in enumerated_doors if not door.is_open]

    def contestant_has_won(self):
        return self.doors[self.contestant_guess].has_prize

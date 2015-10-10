from __future__ import division
import random

from game import Game
from door import Door


def compare_strategies():
    print "Chance of winning when switching: ", simulate(True)
    print "Chance of winning when sticking:  ", simulate(False)

def simulate(contestant_switches):
    results = []
    no_of_trials = 5000
    for _ in range(no_of_trials):
        results.append(play_game(contestant_switches))
    wins = results.count(True)

    return wins / no_of_trials

def play_game(contestant_switches):
    doors = [Door(False), Door(False), Door(True)]
    random.shuffle(doors)

    game = Game(*doors)
    game.contestant_guess = doors[0]
    game.host_open_door()

    if contestant_switches:
        game.contestant_switch()
    return game.contestant_has_won()

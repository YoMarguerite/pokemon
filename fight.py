import random

from player import Player
from enemy import Enemy
from Pokedex import pokedex
from Api import Api

class Fight:

    def __init__(self, joueur):
        self.joueur = joueur
        self.enemy = Enemy("Jean Louis")

        



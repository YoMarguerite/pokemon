from player import Player
from Pokedex import pokedex
from random import *

class Enemy:

    def __init__(self, name):
        self.player = Player(name)
        numberPokemon = randint(2,4)

        pokedex.getPokemon(50)
        for i in range(numberPokemon):
            self.player.addPokemon(pokedex.listePokemon[randint(0,49)])
    
    def displayEnemy(self):
        print("------ Enemy - "+ str(self.player.getName()) +"------")
        for pokemon in self.player.getPokemon():
            print(str(i)+"-"+pokemon.name)
            i+=1
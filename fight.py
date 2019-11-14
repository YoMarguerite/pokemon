import random

from player import Player
from enemy import Enemy
from Pokedex import pokedex
from Api import Api

class Fight:

    def __init__(self, joueur):
        self.joueur = joueur
        self.enemy = Enemy("Jean Louis")
        self.pokemonJoueurOut = []
        self.pokemonEnemyOut = []

    def avantCombat(self):
        print("=======COMBAT=======")
        print("Votre equipe : \n" + self.joueur.displayTeam())
        print("Equipe adverse : \n" + self.enemy.player.displayTeam())
        self.choisirPokemon()
        
        

    def tour(self, pokemon):
        print("Que faire ?")
        print("1 - Attaquer")
        print("2 - Changer de pokemon")
        choix = input("Votre choix : ")
        if choix == "1":
            self.attaquer(pokemon)
        else:
            self.choisirPokemon()

    def attaquer(self, pokemon):
        print()

    def choisirPokemon(self):
        print("Quel pokemon envoyer ?")
        i = 1
        for pokemon in self.joueur.getTeam():
            print(i + " - " + pokemon.getName())
            i+=1
        choix = input("Votre choix : ")
        if choix > 0 and choix <= i:
            if self.pokemonJoueurOut.index(i) == -1:
                pokemon = self.joueur.getPokemon(i-1)
                self.tour(pokemon)
            else:
                print("Le pokemon est mort")
                self.choisirPokemon()
        else:
            print("Choix erroné")
            self.choisirPokemon()




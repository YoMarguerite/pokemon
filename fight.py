from random import *

from player import Player
from enemy import Enemy
from Pokedex import pokedex
from Api import Api

class Fight:

    def __init__(self, joueur):
        self.joueur = joueur
        self.adversaire = Enemy("Jean Louis")
        self.pokemonJoueurOut = []
        self.pokemonEnemyOut = []
        self.idPokemonAdverse = -1
        self.pokemonAdverse = None

    def avantCombat(self):
        print("=======COMBAT=======")
        if len(self.joueur.getTeam()) == 0:
            print("Vous n'avez pas de pokemons")
            self.finDuCombat(False)
        self.choisirPokemon()
        
        

    def tour(self, pokemon):
        while self.idPokemonAdverse == -1 or self.adversaire.player.getTeam()[self.idPokemonAdverse] in self.pokemonEnemyOut:
            self.idPokemonAdverse = randint(0,len(self.adversaire.player.getTeam())-1)
        self.pokemonAdverse = self.adversaire.player.getPokemon(self.idPokemonAdverse)
        print("Pokemon adverse : " + self.pokemonAdverse.getName())
        print("Que faire ?")
        print("1 - Attaquer")
        print("2 - Changer de pokemon")
        choix = input("Votre choix : ")
        if choix == "1":
            self.attaquer(pokemon)
        else:
            self.choisirPokemon()

    def attaquer(self, pokemon):
        print("Quelle attaque faire ?")
        i = 1
        for attack in pokemon.getAttackPoke():
            print(str(i) + " - " + attack.getName())
            i+=1
        choix = int(input("Votre choix : "))
        if choix > 0 and choix <= i:
            self.combat(pokemon.getAttackPokeById(choix), pokemon)
        else:
            print("Choix erroné")
            self.attaquer(pokemon)

    def choisirPokemon(self):
        print("Quel pokemon envoyer ?")
        i = 1
        for pokemon in self.joueur.getTeam():
            print(str(i) + " - " + pokemon.getName())
            i+=1
        choix = int(input("Votre choix : "))
        if choix > 0 and choix <= i:
            if self.joueur.getTeam()[choix-1].getName() not in self.pokemonJoueurOut:
                pokemon = self.joueur.getPokemon(choix-1)
                self.tour(pokemon)
            else:
                print("Le pokemon est mort")
                self.choisirPokemon()
        else:
            print("Choix erroné")
            self.choisirPokemon()

    def combat(self, attackPoke, pokemon):
        power = attackPoke.getPower()
        if power == None:
            power = 0
        if attackPoke.getTypeMove().getName() == pokemon.getTypePoke()[0].getName():
            power = power * 1.5
        if len(pokemon.getTypePoke()) == 2:
            if attackPoke.getTypeMove().getName() == pokemon.getTypePoke()[1].getName():
                power = power * 1.5
        if self.pokemonAdverse.getTypePoke()[0].getName() in attackPoke.getTypeMove().getDoubleDamageTo():
            power = power * 2
        if self.pokemonAdverse.getTypePoke()[0].getName() in attackPoke.getTypeMove().getHalfDamageTo():
            power = power * 0.5
        if len(self.pokemonAdverse.getTypePoke()) == 2:
            if self.pokemonAdverse.getTypePoke()[1].getName() in attackPoke.getTypeMove().getDoubleDamageTo():
                power = power * 2
            if self.pokemonAdverse.getTypePoke()[1].getName() in attackPoke.getTypeMove().getHalfDamageTo():
                power = power * 0.5
        attackEnemyPoke = self.pokemonAdverse.getAttackPokeById(randint(0, len(self.pokemonAdverse.getAttackPoke())-1))
        powerAdverse = attackEnemyPoke.getPower()
        if powerAdverse == None:
            powerAdverse = 0
        if attackEnemyPoke.getTypeMove().getName() == self.pokemonAdverse.getTypePoke()[0].getName():
            powerAdverse = powerAdverse * 1.5
        if len(self.pokemonAdverse.getTypePoke()) == 2:
            if attackEnemyPoke.getTypeMove().getName() == self.pokemonAdverse.getTypePoke()[1].getName():
                powerAdverse = powerAdverse * 1.5
        if pokemon.getTypePoke()[0].getName() in attackEnemyPoke.getTypeMove().getDoubleDamageTo():
            powerAdverse = powerAdverse * 2
        if pokemon.getTypePoke()[0].getName() in attackEnemyPoke.getTypeMove().getHalfDamageTo():
            powerAdverse = powerAdverse * 0.5
        if len(pokemon.getTypePoke()) == 2:
            if pokemon.getTypePoke()[1].getName() in attackEnemyPoke.getTypeMove().getDoubleDamageTo():
                powerAdverse = powerAdverse * 2
            if pokemon.getTypePoke()[1].getName() in attackEnemyPoke.getTypeMove().getHalfDamageTo():
                powerAdverse = powerAdverse * 0.5
        if power >= powerAdverse:
            print("Le pokemon adverse " + self.pokemonAdverse.getName() + " est K.O")
            self.pokemonEnemyOut.append(self.pokemonAdverse.getName())
            if len(self.pokemonEnemyOut) >= len(self.adversaire.player.getTeam()):
                self.finDuCombat(True)          
            else:
                self.tour(pokemon)
        else :
            print("Votre pokemon " + pokemon.getName() + " est K.O")
            self.pokemonJoueurOut.append(pokemon.getName())
            if len(self.pokemonJoueurOut) >= len(self.joueur.getTeam()):
                self.finDuCombat(False)
            else:
                self.choisirPokemon()

    def finDuCombat(self, victoire):
        if victoire == True:
            return print("Victoire!")
        else:
            return print("Défaite!")

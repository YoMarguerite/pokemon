import random

from player import Player
from Pokedex import pokedex
from Api import Api

class Catch:


    pokeball = [{"name" : "pokeball", "proba" : "0.5" },{"name" : "masterball", "proba" : "0.5"}]

    def __init__(self, joueur):
        self.joueur = joueur
        self.pokemon_capture = ""

    def set_joueur(self, joueur):
        self.joueur = joueur

    def set_pokemon_joueur(self, pokemon_joueur):
        self.pokemon_joueur = pokemon_joueur

    def set_pokemon_capture(self):
        pokemon_capture = pokedex.getPokemon(20)
        print(pokemon_capture)
        random_number = len(pokemon_capture)
        self.pokemon_capture = pokemon_capture[random.randint(1, random_number)].name

    def set_pokeball(self):
        self.pokeball = self.joueur.getInventory()

    def get_joueur(self):
        return self.joueur

    def get_pokemon_joueur(self):
        return self.pokemon_joueur

    def get_pokemon_capture(self):
        return self.pokemon_capture

    def get_pokeball(self):
        return self.pokeball

    def avantCapture(self):
        if len(self.pokeball) > 0:
            print("=======CAPTURE=======")
            self.set_pokemon_capture()
            print("Le pokemon est " + self.get_pokemon_capture()["name"])
            print("Voulez vous le capturer ?")
            print("1 - Oui")
            print("2 - Non")
            choix = input("Votre choix : ")
            if choix == "1":
                self.capture()
            else:
                self.retour()
        else:
            print("Aucune pokéball")

    def capturePokeball(self):
        print("Lancer une pokéball")
        print("1 - Oui")
        print("2 - Non")
        choix = input("Votre choix : ")
        all_pokeball = self.pokeball
        if choix == "1":
            i = 0
            for pokeball in all_pokeball:
                print(i, " - ", pokeball["name"])
                i += 1
            number_pokeball = int(input("Sélectionner une pokeball : "))
            random_number = random.uniform(0, 1)
            if random_number < float(all_pokeball[number_pokeball]["proba"]):
                self.joueur.addPokemon(self.pokemon_capture)
                return 2
            else:
                return 1;
        else:
            self.retour()

    def capture(self):
        choix = self.capturePokeball()
        while choix != 2:
            if choix == 1:
                print("Non capturer, voulez vous réessayer ?")
                print("1 - Oui")
                print("2 - Non")
                choixCapture = int(input("Votre choix : "))
                if choixCapture == 1:
                    choix = self.capturePokeball()

    def retour(self):
        return print("Non-capture")


pokemon = Catch(Player("Paul"))
pokemon.set_pokemon_capture()
print(pokemon.get_pokemon_capture())

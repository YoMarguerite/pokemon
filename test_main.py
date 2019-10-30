import os, time
from Api import Api
from player import Player
from Pokedex import Pokedex
from Region import Region

def menu(joueur, region):
    len_nom = len(joueur) + 4
    len_region = len(region) + 4
    print("-" * len_nom + " " + len_region * "-")
    print("| " + joueur + " | | " + region + " | ")
    print("-" * len_nom + " " + len_region * "-")
    print("1 - Aller dans une nouvelle région")
    print("2 - Accèder au Pokedex")
    print("3 - Visualiser un Pokemon du pokedex")

#Initialisation
pokedex = Pokedex()
liste_pokemon = []
liste_pokemon = pokedex.getPokemon(int(input("Renseigner le nombre de pokemons que vous-voulez dans votre monde ?")))

region = Api.callApi("region")
joueur_region = Region()
joueur_region.setRegion(str(region["results"][0]["name"]))
list_region = []
list_region = joueur_region.chargerListRegion(region["results"])

joueur_nom = input("Bonjour nouveau dresseur, pouvons-nous savoir quel est votre nom ?")
joueur = Player(joueur_nom)

#Début du jeu
quitter = False
while quitter == False:
    menu(joueur.getName(), joueur_region.getRegion())
    choix_menu = int(input("Que souhaitez-vous faire ?"))
    os.system('cls') # permet de clear la zone
    if choix_menu == 1:
        choix_region = joueur_region.choixRegion(list_region)
        joueur_region.afficherRegion(choix_region)
        time.sleep(5)
        os.system('cls')
    elif choix_menu == 2:
        pokedex.afficheListe()
    elif choix_menu == 3:
        pokedex.afficheListe()
        choix_pokemon = int(input("Quel pokemon voulez-vous visualiser ?"))
        pokedex.visualiserPokemon(choix_pokemon)
    else:
        print("redemander")
        

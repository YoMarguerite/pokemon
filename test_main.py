import os, time
from Api import Api
from player import Player
from Pokedex import Pokedex
from Pokemon import Pokemon
from Region import Region
from inventory import Inventory
from Shop.Shop import Shop
from fight import Fight

def menu(joueur, region):
    len_nom = len(joueur) + 4
    len_region = len(region) + 4
    print("-" * len_nom + " " + len_region * "-")
    print("| " + joueur + " | | " + region + " | ")
    print("-" * len_nom + " " + len_region * "-")
    print("1 - Aller dans une nouvelle région")
    print("2 - Accèder au Pokedex")
    print("3 - Visualiser un Pokemon du pokedex")
    print("4 - Joueur")
    print("5 - Boutique")
    print("7 - Combat")
    print("6- Quitter")

#Initialisation
pokedex = Pokedex()
liste_pokemon = []
liste_pokemon = pokedex.getPokemon(int(input("Renseigner le nombre de pokemons que vous-voulez dans votre monde ?")))

inventory = Inventory(10)
shop = Shop()
region = Api.callApi("region")
joueur_region = Region()
joueur_region.setRegion(str(region["results"][0]["name"]))
list_region = []
list_region = joueur_region.chargerListRegion(region["results"])

joueur_nom = input("Bonjour nouveau dresseur, pouvons-nous savoir quel est votre nom ?")
joueur = Player(joueur_nom)
joueur.addPokemon(Pokemon(1, "chimchar", "https://pokeapi.co/api/v2/pokemon/390/"))

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
    elif choix_menu == 4:
        joueur.menu()
    elif choix_menu == 5:
        action = int(input("Voulez-vous acheter (1) ou vendre ? (2)"))
        if action == 1:
            print("Que voulez-vous acheter ?")
            for item in shop.getListItem():
                print(str(item.getId()) + " - " + item.getName() + " | " + str(item.getCost()))
            ids = int(input("Choisissez ce que vous voulez acheter"))
            item = shop.getById(ids)
            inventory.addItem(item)
            joueur.setCredit(joueur.getCredit() - item.getCost())
        elif action == 2:
            print("Choissisez un objet à vendre : ")
            inventory.displayItem()
            ids = int(input("Quel objet voulez-vous vendre ?"))

            shop.sell(joueur, inventory.getById(ids))
            inventory.delItem(inventory.getById(ids))
    elif choix_menu == 6:
        print("Bye bye !")
        quitter = True
    elif choix_menu == 7:
        combat = Fight(joueur)
        combat.avantCombat()
    else:
        print("redemander")

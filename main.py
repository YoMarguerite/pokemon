from player import Player
from Pokedex import pokedex


def init():
    player = Player(input("Quel est votre nom ?"))
    return player

# menu pas terminé
def menu():
    print("### - Menu - ###")
    print("#              #")
    print("# 0 - Pokedex  #")
    print("# 1 - ???      #")
    print("# 2 - ???      #")
    print("# 3 - Quitter  #")
    print("#              #")
    print("###----------###")

def main():
    player = init()
    choix = 0
    while choix != 3:
        menu()
        choix = int(input("Que voulez vous faire ?")) 
        if choix == 0:
            pokedex.visualiserPokemon(1)
    print("Bye bye !")

main()
from inventory import Inventory
from Pokemon import Pokemon
import os

class Player:

    def __init__(self, name):
        self.name = name
        self.credit = 0
        self.team = []
        self.ordi = []
        # self.ordi = Ordi()
        self.inventory = Inventory(50)

    def getName(self):
        return self.name

    def getCredit(self):
        return self.credit
    
    def setCredit(self, credit):
        self.credit = credit

    def addCredit(self, nb):
        self.credit = self.credit + nb

    def getInventory(self):
        return self.inventory

    def getPokemon(self, index):
        if ((0 <= index)and(index<=len(self.team))):
            return self.team[index]

    def getTeam(self):
        return self.team
    
    def addPokemon(self, pokemon):
        if (pokemon not in self.team)and(pokemon not in self.ordi):
            if (len(self.team) == 6):
                self.ordi.append(Pokemon(1,pokemon["name"],pokemon["url"]))
                print(pokemon["name"]+" a été ajouté à l'ordi.")
            else:
                self.team.append(Pokemon(1,pokemon["name"],pokemon["url"]))
                print(pokemon["name"]+" a été ajouté à l'équipe.")
        else:
            print("Vous possédez déjà "+pokemon.name)

    def delPokemon(self, index):
        if ((0 <= index)and(index<=len(self.team))):
            pokemon = self.team[index]
            del self.team[index]
            print(pokemon.name+" a bien été supprimé.")
    
    def displayTeam(self):
        os.system('cls')
        if len(self.team)>0:
            i = 0
            print("------TEAM------")
            for pokemon in self.team:
                print(str(i)+"-"+pokemon)
                i+=1
        else:
            print("Votre équipe est vide...")
    
    def menu(self):
        retour = False
        while retour == False:
            os.system('cls')
            print("JOUEUR - "+self.getName())
            print("Vous avez "+str(self.getCredit())+"€")
            print("1 - Afficher l'équipe pokemon")
            print("2 - Inventaire")
            print("3 - Retour")
            choix_menu = int(input("Que souhaitez-vous faire ?"))
            os.system('cls')
            if choix_menu == 1:
                self.displayTeam()
                os.system('cls')
            elif choix_menu == 2:
                self.getInventory().menu()
                os.system('cls')
            elif choix_menu == 3:
                retour = True
                


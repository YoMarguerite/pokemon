from inventory import Inventory

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
    
    def addPokemon(self, pokemon):
        if (pokemon not in self.team)and(pokemon not in self.ordi):
            if (len(self.team) == 6):
                self.ordi.append(pokemon)
                print(pokemon["name"]+" a été ajouté à l'ordi.")
            else:
                self.team.append(pokemon)
                print(pokemon["name"]+" a été ajouté à l'équipe.")
        else:
            print("Vous possédez déjà "+pokemon.name)

    def delPokemon(self, index):
        if ((0 <= index)and(index<=len(self.team))):
            pokemon = self.team[index]
            del self.team[index]
            print(pokemon.name+" a bien été supprimé.")
    
    def displayTeam(self):
        i = 0
        print("------TEAM------")
        for pokemon in self.team:
            print(str(i)+"-"+pokemon.name)
            i+=1
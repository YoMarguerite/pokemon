

class Player:

    def __init__(self, name):
        self.name = name
        self.credit = 0
        self.team = []
        self.ordi = []
        self.inventory = Inventory()

    def getName(self):
        return self.name

    def getCredit(self):
        return self.credit
    
    def setCredit(self, credit):
        self.credit = credit

    def getPokemon(self, index):
        if ((0 <= index)and(index<=len(self.team))):
            return self.team[index]
    
    def addPokemon(self, pokemon):
        if (pokemon not in self.team)and(pokemon not in self.ordi):
            if (len(self.team) == 6):
                self.ordi.append(pokemon)
                print(pokemon.name+" a été ajouté à l'ordi.")
            else:
                self.team.append(pokemon)
                print(pokemon.name+" a été ajouté à l'équipe.")
        else:
            print("Vous possédez déjà "+pokemon.name)
    
    def displayTeam(self):
        i = 0
        print("------TEAM------")
        for pokemon in self.team:
            print(str(i)+"-"+pokemon.name)
            i+=1

class Inventory:
    def __init__(self):
        pass
# class pokemon:
#     def __init__(self, name):
#         self.name = name

# pokemon = pokemon("salamanche")
# player = Player("yop")
# print(player.getName())
# player.addPokemon(pokemon)
# player.addPokemon(pokemon)
# player.displayTeam()
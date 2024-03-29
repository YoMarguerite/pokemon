from Shop.Items import Items
import os

class Inventory:
    def __init__(self, limit):
        self.items = []
        self.limit = limit

    def getItem(self, index):
        if 0<=index and index<len(self.items):
            return self.items[index]

    def getPokeball(self):
        pokeball =  [
                        {"name" : "pokeball", "proba" : "0.5" },
                        {"name" : "superball", "proba" : "0.7" },
                        {"name" : "hyperball", "proba" : "0.85"},
                        {"name" : "masterball", "proba" : "1"}
                    ]
        for item in self.items:
            if item.getCategory().getName() == "standard-balls":
                pokeball.append(item)
        return pokeball

    def addItem(self, item):
        try:
            if item not in self.items:
                if len(self.items) < self.limit:
                    self.items.append(item)
                    print(item.getName()+" a été ajouté à l'inventaire.")
                else:
                    print("Votre inventaire est plein.")
            else:
                print("Vous avez déjà cet objet.")
        except:
            print("Erreur l'objet n'a pas pu être ajouté à l'inventaire.")

    def delItem(self, item):
        try:
            if item in self.items:
                self.items.remove(item)
                print("1 " + str(item.getName()) + " a été supprimé de l'inventaire.")
            else:
                print("Cet objet n'existe pas.")
        except:
            print("L'item n'a pas pu être supprimé de l'inventaire.")

    def displayItem(self):
        os.system('cls')
        i = 0
        print("------INVENTAIRE------")
        for item in self.items:
            print(str(item.getId()) + " " + item.getName())
            i+=1

    def getItems(self):
        return self.items
    
    def menu(self):
        retour = False
        while retour == False:
            self.displayItem()
            print(str(len(self.items))+" - Retour" )
            choix_item = int(input("Choisissez un item :"))
            if choix_item == len(self.items):
                retour = True
            else:
                print("à voir si on rajoute des actions sur les objets")
                print(self.getItem(choix_item).getName())

    def getById(self, ids):
        for item in self.getItems():
            if item.id == ids:
                return item


class Inventory:
    def __init__(self, limit):
        self.items = []
        self.limit = limit
    
    def getItem(self, index):
        if 0<=index and index<len(self.items):
            return self.items[index]
    
    def getPokeball(self):
        pokeball = []
        for item in self.items:
            if type(item) == "pokeball"
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
            print(item.getName()+" n'a pas pu être ajouté à l'inventaire.")
    
    def delItem(self, index):
        try:
            if 0<=index and index<len(self.items):
                item = self.items[index]
                del self.items[index]
                print(item.getName()+" a été supprimé de l'inventaire.")
            else:
                print("Cet objet n'existe pas.")
        except:
            print("L'item n'a pas pu être supprimé de l'inventaire.")

    def displayItem(self):
        i = 0
        print("------INVENTAIRE------")
        for item in self.items:
            print(str(i)+"-"+item.name)
            i+=1
        
    

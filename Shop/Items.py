from Shop import ItemCategory


class Items:
    name = '',
    cost = 0,
    category = ItemCategory

    def __init__(self, name, cost):
        self.id = id,
        self.name = name,
        self.cost = cost

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

    def getCategory(self):
        return self.category

    def setCategory(self, category):
        self.category = category

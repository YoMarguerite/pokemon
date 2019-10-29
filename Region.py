class Region:
    def __init__(self):
        self.name = ""

    def getRegion(self):
        return self.name

    def setRegion(self, name):
        self.name = name

    def choixRegion(self, list_region):
        i = 1
        for name in list_region:
            print(str(i) + " : " + name)
            i = i + 1
        choix_user = int(input("Où voulez-vous allez ?"))
        self.setRegion(str(list_region[choix_user - 1]))

        
    def chargerListRegion(self, list_api):
        list_region = []
        for name in list_api:
            list_region.append(name["name"])
        return list_region
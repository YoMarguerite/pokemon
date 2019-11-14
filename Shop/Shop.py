from Api import Api
from Shop.ItemCategory import ItemCategory
from Shop.Items import Items


class Shop:
    listItems = []
    listCategory = []

    def __init__(self):
        self.filllistitem()
        self.filllistcategory()

    def filllistitem(self):
        results = Api.callApi('item/').get('results')
        i = 1
        for items in results:
            # Récupérer les détails de l'Item en appelant l'URL de détails
            item = Api.callApi(items.get('url'))
            # ajouter à la liste d'Item de la boutique
            self.listItems.append(Items(i, item.get('name'), item.get('cost')))
            i = i + 1

    def filllistcategory(self):
        """
        :return: void
        """
        results = Api.callApi('item-category/').get('results')
        for cat in results:
            self.listCategory.append(ItemCategory(cat.get('name')))

    def getListItem(self):

        """
        :rtype: Items[]
        """
        return self.listItems

    def getListCategory(self):
        return self.listCategory

    def buy(self, player, item):
        """
        :type player: Player
        :type item: Items
        """
        player.getInventory().addItem(item)

    def sell(self, player, item):
        """

        :param player: Player
        :param item: Items
        """
        if item.getCost() > 0:
            amount = item.getCost * 0.20
            player.addCredit(amount)
            print("Vous avez vendu l'objet " + item.getName())

    def getById(self, ids):
        for item in self.listItems:
            if item.id == ids:
                return item



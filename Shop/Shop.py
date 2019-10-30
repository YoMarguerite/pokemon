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
        for items in results:
            # Récupérer les détails de l'Item en appelant l'URL de détails
            item = Api.callApi(items.get('url'))
            # ajouter à la liste d'Item de la boutique
            self.listItems.append(Items(item.get('name'), item.get('cost')))

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
        player.getInventory().addsdItem(item)

    def sell(self, player, item):
        """

        :param player: Player
        :param item: Items
        """
        if item.getCost() > 0:
            amount = item.getCost * 0.20
            player.addCredit(amount)
            ("Vous avez vendu l'objet " + item.getName())

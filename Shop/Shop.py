from Api import Api
from Shop.ItemCategory import ItemCategory
from Shop.Items import Items


class Shop:
    listItems = []
    listCategory = []

    def __init__(self):
        self.filllistitem()

    def filllistitem(self):
        results = Api.callApi('item/').get('results')
        for items in results:
            # Récupérer les détails de l'Item en appelant l'URL de détails
            item = Api.callApi(items.get('url'))
            # ajouter à la liste d'Item de la boutique
            self.listItems.append(Items(item.get('name'), item.get('cost')))

    def filllistcategory(self):
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

    def buy(self):
        print('Acheter')

    def sell(self):
        print('Vendre')

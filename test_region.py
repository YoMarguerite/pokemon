import requests
from Region import Region
from Api import Api

# r = requests.get("https://pokeapi.co/api/v2/region?limit=20")
# region = r.json()

region = Api.callApi("region")


print("BIENVENUE DANS POKEMON")
print("MENU")

#je créé un objet region
user_region = Region()
# j'initialise la region au premier élément de la liste car voilà faut bien commencer quelque part
user_region.setRegion(str(region["results"][0]["name"]))
# j'affiche la localisation actuelle mais celle-ci sera mieux affiché
print("Vous êtes actuellement à : " + user_region.getRegion())
# j'initialise une liste qui prendra la les infos de l'api pour y avoir accès une seule fois
list_region = []
list_region = user_region.chargerListRegion(region["results"])
# lors d'une demande user pour changer de lieux, il faut passer par cette méthode qui : 
#   - affiche les lieux
#   - demande au user de choisir
#   - change sa localisation
user_region.choixRegion(list_region)

# petite affichage montrant qu'on a bien changer d'endroit
print("Vous êtes maintenant à " + str(user_region.getRegion()))

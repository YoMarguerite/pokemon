from Api import Api
from Pokemon import Pokemon
from Pokedex import Pokedex

print("--------------- Voici le pokedex ---------------")
listePokemon = []
unPokedex = Pokedex("pokedex",listePokemon)
pokemonsAPI = Api.callApi("pokemon?limit=20")
i=0

for pokemon in pokemonsAPI["results"]:
    print("Le n°"+ str(i) +" est : "+ pokemon["name"])
    i=i+1
    unPokemon = Pokemon(i, pokemon["name"], pokemon["url"])
    listePokemon.append(unPokemon)
    #print(listePokemon)
   
    

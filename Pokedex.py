from Api import Api
from Pokemon import Pokemon

class Pokedex: 
    def __init__(self, nom):
         self.nom = nom
         self.listePokemon = []
         print("--------------- Creation du pokedex ---------------")
    
    def getPokemon(self,max):
     pokemonsAPI = Api.callApi("pokemon?limit="+str(max))
     i=0
     print("--------------- Le pokedex contient les pokemons suivants---------------")
     for pokemon in pokemonsAPI["results"]:
         #print("Le n°"+ str(i) +" est : "+ pokemon["name"])
         i=i+1
         unPokemon = Pokemon(i, pokemon["name"], pokemon["url"])
         self.listePokemon.append(unPokemon)
    
    def afficheListe(self):
     i = 0
     for pokemon in self.listePokemon:
         print("Le n°"+ str(pokemon.getId()) +" est : "+ pokemon.getName() + " et il est de type :"+ pokemon.getTypePoke())
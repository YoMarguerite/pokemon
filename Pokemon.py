from Api import Api
import requests
class Pokemon: 
  
     def __init__(self, id, nom,url):
        self.id = id
        self.nom = nom
        self.url = url
        pokemonDetails = requests.get(url)
        #print(pokemonDetails.json())
        j = 0
        typePoke = pokemonDetails.json()
        #print(typePoke["types"])
        for pokemon in typePoke["types"][j]:
            #tester si le deuxième tyes existe
         #   print("j = " + str(j))
          #  print(pokemon) 
#            self.typePoke = self.typePoke + str(pokemon)
            j=j+1
 
         
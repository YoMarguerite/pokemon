from Api import Api
import requests

class TypePokemon:

   def __init__(self, name, url):
      self.id = id
      self.name = name
      self.url = url
      pokemonDetails = requests.get(url)
      typePokejson = pokemonDetails.json()
      self.doubleDamageTo = []
      self.halfDamageTo = []
      for types in typePokejson["damage_relations"]['double_damage_to']:
        self.doubleDamageTo.append(types['name'])
      for types in typePokejson["damage_relations"]['half_damage_to']:
        self.halfDamageTo.append(types['name'])

   def getName(self):
      return self.name
   def setName(self, name):
      self.name = name

   def getUrl(self):
      return self.url
   def setUrl(self, url):
      self.url = url

   def getDoubleDamageTo(self):
      return self.doubleDamageTo
   def setDoubleDamageTo(self, doubleDamageTo):
      self.doubleDamageTo = doubleDamageTo

   def getHalfDamageTo(self):
      return self.halfDamageTo
   def setHalfDamageTo(self, halfDamageTo):
      self.halfDamageTo = halfDamageTo
from Api import Api
import requests
from typePokemon import TypePokemon

class Move:
   def __init__(self, name, url):
      self.id = id
      self.name = name
      self.url = url
      pokemonDetails = requests.get(url)
      typePokejson = pokemonDetails.json()
      self.power = typePokejson["power"]
      self.typeMove = TypePokemon(typePokejson['type']['name'], typePokejson['type']['url'])
      

   def getName(self):
      return self.name
   def setName(self, name):
      self.name = name

   def getUrl(self):
      return self.url
   def setUrl(self, url):
      self.url = url

   def getPower(self):
      return self.power
   def setPower(self, power):
      self.power = power

   def getTypeMove(self):
      return self.typeMove
   def setTypeMove(self, typeMove):
      self.typeMove = typeMove
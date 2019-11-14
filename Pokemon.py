from Api import Api
import requests
from typePokemon import TypePokemon
from move import Move

class Pokemon:
   def __init__(self, id, name, url):
      self.id = id
      self.name = name
      self.url = url
      pokemonDetails = requests.get(url)
      i = 0
      typePokejson = pokemonDetails.json()
      self.typePoke = []
      self.attackPoke = []
      for types in typePokejson["types"]:
         self.typePoke.append(TypePokemon(types['type']['name'], types['type']['url']))
      for move in typePokejson["moves"]:
         if i < 7:
            self.attackPoke.append(Move(move['move']['name'],move['move']['url']))
            i=i+1

   def getId(self):
      return self.id 
   def setId(self, id ):
      self.id == id

   def getName(self):
      return self.name
   def setName(self, name):
      self.name = name

   def getUrl(self):
      return self.url
   def setUrl(self, url):
      self.url = url

   def getTypePoke(self):
      return self.typePoke
   def setTypePoke(self, typePoke):
      self.typePoke = typePoke

   def getAttackPoke(self):
      return self.attackPoke
   def setAttackPoke(self, attackPoke):
      self.attackPoke = attackPoke
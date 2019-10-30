from Api import Api
import requests
class Pokemon:
   def __init__(self, id, name,url):
      self.id = id
      self.name = name
      self.url = url
      pokemonDetails = requests.get(url)
      j = 0
      i = 0
      typePokejson = pokemonDetails.json()
      typePoke = ''
      for pokemon in typePokejson["types"]:
         typePoke = typePoke + pokemon['type']['name'] + ' '
         j=j+1
         #print(typePoke)            
      self.typePoke = typePoke
      attackPoke = ''
      for pokemon in typePokejson["moves"]:
         if i < 8:
            attackPoke = attackPoke + pokemon['move']['name'] + '  '
            i=i+1
            #print(attackPoke)
      self.attackPoke = attackPoke 
   
   def getId(self):
        return self.id 
   def setId(self, id ):
      self.id = id
   
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
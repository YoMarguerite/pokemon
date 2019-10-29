import requests
from requests.exceptions import HTTPError
import json


class Api:

    # Exemple d'apel à l'API : bulbasaur = Api.callApi("pokemon/1/")
    # PS : Vous pouvez maintenant mettre une url complète comprenant "http" ou continuer à mettre le endpoint.
    # l'URL complète peut-être utile dans le cas ou vous récupérez l'URL complète dans un objet
    @staticmethod  # rendre la méthode static
    def callApi(endpoint):
        if 'http' in endpoint:
            baseURI = ''
        else:
            baseURI = "https://pokeapi.co/api/v2/"
        try:
            response = requests.get(baseURI + endpoint)
        except HTTPError as httpErr:
            print("GET: HTTP Error : {httpErr}")
        except Exception as e:
            print("GET: HTTP FATAL Error : " + e)
        else:
            return json.loads(response.text)

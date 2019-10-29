import requests
from requests.exceptions import HTTPError
import json


class Api:

    # Exemple d'apel à l'API : bulbasaur = Api.callApi("pokemon/1/")

    @staticmethod  # rendre la méthode static
    def callApi(endpoint):
        baseURI = "https://pokeapi.co/api/v2/"
        try:
            response = requests.get(baseURI + endpoint)
        except HTTPError as httpErr:
            print("GET: HTTP Error : {httpErr}")
        except Exception as e:
            print("GET: HTTP FATAL Error : " + e)
        else:
            return json.loads(response.text)

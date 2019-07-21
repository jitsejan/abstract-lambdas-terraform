""" jokeapiresolver.py """
import os
import requests


class JokeApiResolver:
    """ Class definition for the JokeApiResolver """
    BASE_URL = 'https://official-joke-api.appspot.com/{endpoint}'
    HEADERS = None

    def _get_api_json_response(self, endpoint, data=None):
        """ Return the API JSON response """
        response = requests.get(url=self.BASE_URL.format(endpoint=endpoint),
                                data=data,
                                headers=self.HEADERS)
        return response.json()

    def get_programming_joke(self):
        endpoint = 'jokes/programming/random'
        return self._get_api_json_response(endpoint)

    def get_random_joke(self):
        endpoint = 'random_joke'
        return self._get_api_json_response(endpoint)

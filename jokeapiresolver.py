""" jokeapiresolver.py """
from abstractapiresolver import AbstractApiResolver


class JokeApiResolver(AbstractApiResolver):
    """ Class definition for the JokeApiResolver """

    def get_programming_joke(self):
        endpoint = 'jokes/programming/random'
        return self._get_api_json_response(endpoint)

    def get_random_joke(self):
        endpoint = 'random_joke'
        return self._get_api_json_response(endpoint)

    @property
    def headers(self):
        return None

    @property
    def base_url(self):
        return 'https://official-joke-api.appspot.com/{endpoint}'

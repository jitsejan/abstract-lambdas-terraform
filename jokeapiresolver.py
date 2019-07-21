""" jokeapiresolver.py """
from abstractapiresolver import AbstractApiResolver


class JokeApiResolver(AbstractApiResolver):
    """ Class definition for the JokeApiResolver """

    def get_data(self, endpoint, **params):
        """ Get data from the API """
        url = self.endpoints[endpoint]['url']
        return self._get_api_json_response(url)

    @property
    def base_url(self):
        return 'https://official-joke-api.appspot.com/{endpoint}'

    @property
    def endpoints(self):
        return {
            'get_programming_joke': {
                'data': None,
                'url': 'jokes/programming/random',
            },
            'get_random_joke': {
                'data': None,
                'url': 'random_joke',
            }
        }

    @property
    def headers(self):
        return None

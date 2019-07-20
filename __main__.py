""" __main__.py """
import json
import os
import requests


class IGDBApiResolver:
    """ Class definition for the IGDBApiResolver """
    BASE_URL = 'https://api-v3.igdb.com/{endpoint}'
    HEADERS = {
        'user-key': os.environ.get('IGDB_KEY', '')
    }

    def _get_api_json_response(self, endpoint, data):
        """ Return the API JSON response """
        response = requests.get(url=self.BASE_URL.format(endpoint=endpoint),
                                data=data,
                                headers=self.HEADERS)
        return response.json()

    def get_games(self, platform_id, name=None):
        """ Get the games for a given platform and an optional name filter """
        endpoint = 'games'
        if name:
            query = 'fields name; where name ~ *"{name}"* & platforms = {platform_id}; limit 50;'
        else:
            query = 'fields name; where platforms = {platform_id}; limit 50;'

        return self._get_api_json_response(endpoint=endpoint,
                                           data=query.format(name=name,
                                                             platform_id=platform_id))

    def get_platform_id(self, platform_abbreviation):
        """ Get the platform ID for a given platform abbreviation """
        endpoint = 'platforms'
        query = 'fields id; where abbreviation = "{abbr}";'

        return self._get_api_json_response(endpoint=endpoint,
                                           data=query.format(abbr=platform_abbreviation))[0]['id']


def main():
    """ Main function """
    game_api = IGDBApiResolver()
    platform_id = game_api.get_platform_id("N64")
    games = game_api.get_games(platform_id, "Mario")
    print(json.dumps(games))


if __name__ == "__main__":
    main()

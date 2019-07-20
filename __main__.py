""" __main__.py """
import json
import os
import requests

BASE_URL = 'https://api-v3.igdb.com/{endpoint}'
HEADERS = {
    'user-key': os.environ.get('IGDB_KEY', '')
}


def _get_games(platform_id, name=None):
    """ Get the games for a given platform and an optional name filter """
    endpoint = 'games'
    if name:
        query = 'fields name; where name ~ *"{name}"* & platforms = {platform_id}; limit 50;'
    else:
        query = 'fields name; where platforms = {platform_id}; limit 50;'
    response = requests.get(BASE_URL.format(endpoint=endpoint),
                            data=query.format(name=name, platform_id=platform_id),
                            headers=HEADERS)
    return response.json()


def _get_platform_id(platform_abbreviation):
    """ Get the platform ID for a given platform abbreviation """
    endpoint = 'platforms'
    query = 'fields id; where abbreviation = "{abbr}";'
    response = requests.get(BASE_URL.format(endpoint=endpoint),
                            data=query.format(abbr=platform_abbreviation),
                            headers=HEADERS)
    return response.json()[0]["id"]


def main():
    """ Main function """
    platform_id = _get_platform_id("N64")
    games = _get_games(platform_id, "Mario")
    print(json.dumps(games))


if __name__ == "__main__":
    main()

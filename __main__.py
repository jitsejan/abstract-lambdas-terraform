""" __main__.py """
import os
import requests

BASE_URL = 'https://api-v3.igdb.com/{endpoint}'
HEADERS = {
    'user-key': os.environ.get('IGDB_KEY', '')
}


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
    print(_get_platform_id("N64"))


if __name__ == "__main__":
    main()

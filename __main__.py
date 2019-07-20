import os
import requests

BASE_URL = 'https://api-v3.igdb.com/{endpoint}'
HEADERS = {
    'user-key': os.environ.get('IGDB_KEY', '')
}


def main():
    """ Main function """
    response = requests.get(BASE_URL.format(endpoint='platforms'),
                            data='fields id; where abbreviation = "N64";',
                            headers=HEADERS)
    print(response.json())


if __name__ == "__main__":
    main()
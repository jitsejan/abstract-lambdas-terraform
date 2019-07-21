""" __main__.py """
import json
from igdbapiresolver import IGDBApiResolver
from jokeapiresolver import JokeApiResolver

def main():
    """ Main function """
    game_api = IGDBApiResolver()
    platform_id = game_api.get_data(endpoint="get_platform_id",
                                    abbr="N64")[0]['id']
    games = game_api.get_data(endpoint="get_games_for_platform_with_name",
                              platform_id=platform_id,
                              name="Mario")
    print(json.dumps(games))

    joke_api = JokeApiResolver()
    print(json.dumps(joke_api.get_data(endpoint='get_random_joke')))
    print(json.dumps(joke_api.get_data(endpoint='get_programming_joke')))


if __name__ == "__main__":
    main()

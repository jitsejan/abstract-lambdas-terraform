""" __main__.py """
import json
from igdbapiresolver import IGDBApiResolver
from jokeapiresolver import JokeApiResolver

def main():
    """ Main function """
    game_api = IGDBApiResolver()
    platform_id = game_api.get_platform_id("N64")
    games = game_api.get_games(platform_id, "Mario")
    print(json.dumps(games))

    joke_api = JokeApiResolver()
    print(json.dumps(joke_api.get_random_joke()))
    print(json.dumps(joke_api.get_programming_joke()))


if __name__ == "__main__":
    main()

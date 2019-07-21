""" __main__.py """
import json
from igdbapiresolver import IGDBApiResolver


def main():
    """ Main function """
    game_api = IGDBApiResolver()
    platform_id = game_api.get_platform_id("N64")
    games = game_api.get_games(platform_id, "Mario")
    print(json.dumps(games))


if __name__ == "__main__":
    main()

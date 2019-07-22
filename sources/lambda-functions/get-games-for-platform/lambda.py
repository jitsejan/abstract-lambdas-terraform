""" get_games_for_platform.py """
import json
from abstractlayer.igdbapiresolver import IGDBApiResolver


def lambda_handler(event, context):
    """ Main function """
    game_api = IGDBApiResolver()
    platform_id = game_api.get_data(
        endpoint="get_platform_id", abbr=event.get("platform_abbr", "")
    )[0]["id"]
    games = game_api.get_data(
        endpoint="get_games_for_platform_with_name",
        platform_id=platform_id,
        name=event.get("name", ""),
    )
    print(json.dumps(games))


if __name__ == "__main__":
    event = {"platform_abbr": "N64", "name": "Mario"}
    lambda_handler(event, {})

""" get_programming_joke.py """
import json
from abstractlayer.jokeapiresolver import JokeApiResolver


def lambda_handler(event, context):
    """ Main function """
    joke_api = JokeApiResolver()
    print(json.dumps(joke_api.get_data(endpoint="get_programming_joke")))


if __name__ == "__main__":
    lambda_handler({}, {})

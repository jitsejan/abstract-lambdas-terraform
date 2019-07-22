""" igdbapiresolver.py """
import os
from abstractapiresolver import AbstractApiResolver


class IGDBApiResolver(AbstractApiResolver):
    """ Class definition for the IGDBApiResolver """

    def get_data(self, endpoint, **params):
        """ Get data from the API """
        url = self.endpoints[endpoint]["url"]
        data = self.endpoints[endpoint]["data"].format(**params)
        return self._get_api_json_response(url, data)

    @property
    def base_url(self):
        return "https://api-v3.igdb.com/{endpoint}"

    @property
    def endpoints(self):
        return {
            "get_platform_id": {
                "data": 'fields id; where abbreviation = "{abbr}";',
                "url": "platforms",
            },
            "get_games_for_platform": {
                "data": "fields name; where platforms = {platform_id}; limit 50;",
                "url": "games",
            },
            "get_games_for_platform_with_name": {
                "data": 'fields name; where name ~ *"{name}"* & platforms = {platform_id}; limit 50;',
                "url": "games",
            },
        }

    @property
    def headers(self):
        return {"user-key": os.environ.get("IGDB_KEY", "")}

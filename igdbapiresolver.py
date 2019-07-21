""" igdbapiresolver.py """
import os
from abstractapiresolver import AbstractApiResolver


class IGDBApiResolver(AbstractApiResolver):
    """ Class definition for the IGDBApiResolver """

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

    @property
    def headers(self):
        return {
            'user-key': os.environ.get('IGDB_KEY', '')
        }

    @property
    def base_url(self):
        return 'https://api-v3.igdb.com/{endpoint}'

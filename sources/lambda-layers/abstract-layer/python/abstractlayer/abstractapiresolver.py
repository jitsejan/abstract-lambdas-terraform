""" abstractapiresolver.py """
from abc import ABCMeta, abstractmethod
import requests


class AbstractApiResolver(metaclass=ABCMeta):
    """ Class definition of the AbstractApiResolver """

    def _get_api_json_response(self, endpoint, data=None):
        """ Return the API JSON response """
        response = requests.get(
            url=self.base_url.format(endpoint=endpoint), data=data, headers=self.headers
        )
        return response.json()

    @abstractmethod
    def get_data(self):
        pass

    @property
    @abstractmethod
    def headers(self):
        pass

    @property
    @abstractmethod
    def base_url(self):
        pass

    @property
    @abstractmethod
    def endpoints(self):
        pass

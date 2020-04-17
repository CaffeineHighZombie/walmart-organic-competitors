import requests
import json

API_URL = "http://api.walmartlabs.com/v1/"

class WalapiException(Exception):
    """
    Placeholder Exception class
    """
    def __int__(self, status_code):
        error_message = f"Request failed with the status code: {status_code}"
        super(self.__class__, self).__init__(error_message)

class Walapi:
    
    def __init__(self, api_key):
        """
        :param api_key:
            Walmart Open API key
        """
        self.api_key = api_key
    
    def product_lookup(self, product_id, **kwargs):
        lookup_url = f"{API_URL}items/{product_id}"
        params = {"apiKey": self.api_key}
        r = requests.get(lookup_url, params=params)
        if r.status_code == 200:
            return r.json()
        else:
            raise WalapiException(r.status_code)

    def product_search(self, query, **kwargs):
        search_url = f"{API_URL}search"
        params = {"apiKey": self.api_key}
        params["query"] = query
        params.update(kwargs)
        r = requests.get(search_url, params=params)
        if r.status_code == 200:
            return r.json()
        else:
            raise WalapiException(r.status_code)


class Queryapi(Walapi):

    def __init__(self, rate_limit_delay=0.220):
        pass


import requests
import json
from time import sleep

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

    def __init__(self, api_key, rate_limit_delay=0.220):
        """
        :param api_key:
            Walmart Open API key
        :param rate_limit_delay:
            Delay to respect Walmart Open API rate limit of 5 call per second
        """
        super().__init__(api_key)
        self.rate_limit_delay = rate_limit_delay
        
    def build_per_title_ranking(self, title, search_depth, **kwargs):
        ranking = {}

        num_item_per_search = 10
        start_index = 0
        paging = int(search_depth/num_item_per_search)

        while start_index < paging:
            try:
                start_pointer = start_index * num_item_per_search + 1
                max_rank_on_page = search_depth + 1 - start_pointer
                self._delay()
                result = self.product_search(query=title, start=start_pointer)
                if "items" in result:
                    for i, item in enumerate(result["items"]):
                        ranking[item["itemId"]] = max_rank_on_page - i
            except WalapiException as e:
                pass
            finally:
                start_index += 1
        return ranking

    def build_ranking(self, titles, search_depth, **kwargs):
        ranking = {}
        for title in titles[:search_depth]:
            ranking[title] = self.build_per_title_ranking(title, search_depth)
        return ranking

    def consolidate_ranking(self, ranking, search_depth, **kwargs):
        flat_ranking = {}
        for title, title_ranking in ranking.items():
            for key, value in title_ranking.items():
                if key not in flat_ranking:
                    flat_ranking[key] = value
                else:
                    flat_ranking[key] += value
        final_ranking = {}
        for key, value in flat_ranking.items():
            final_ranking[key] = search_depth - float(value)/search_depth
        return final_ranking

    def get_ranking(self, product_id, **kwargs):
        keyword_search_depth = 10  ## As per challenge specification
        if "keyword_search_depth" in kwargs:
            keyword_search_depth = kwargs["keyword_search_depth"]
        data = self.product_lookup(product_id)
        product_title = data["name"]
        titles = product_title.split()
        keyword_ranking = self.build_ranking(titles, keyword_search_depth)
        final_ranking = self.consolidate_ranking(keyword_ranking, keyword_search_depth)
        return final_ranking

    def _delay(self):
        sleep(self.rate_limit_delay)


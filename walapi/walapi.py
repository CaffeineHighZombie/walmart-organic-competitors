
import requests
import json
from time import sleep

API_BASE_URL='http://api.walmartlabs.com/v1/'
params = {'apiKey': 'ufrfxx5tg4uc9cx6pjsq97b2', 'format': 'json'}

def product_lookup(productId):
    lookup_url = f"{API_BASE_URL}items/{productId}"
    r = requests.get(lookup_url, params=params)
    # print("In product lookup with status code", r.status_code)
    data = r.json()
    return data

def search(query, start=1):
    search_url = f"{API_BASE_URL}search"
    params["query"] = query
    params["start"] = start
    r = requests.get(search_url, params=params)
    # print("In search with status code", r.status_code)
    data = r.json()
    return data

def build_per_title_ranking(title):
    ranking = {}
    sleep(0.100)
    result = search(title)
    try:
        for i, item in enumerate(result["items"]):
            ranking[item["itemId"]] = 20-i
    except Exception as e:
        # print(e)
        pass
    sleep(0.100)
    result = search(query=title, start = 10)
    try:
        for i, item in enumerate(result["items"]):
            ranking[item["itemId"]] = 10-i
    except Exception as e:
        # print(e)
        pass
    return ranking

def build_ranking(titles):
    ranking = {}
    for title in titles:
        ranking[title] = build_per_title_ranking(title)
    return ranking


def consolidate_ranking(ranking):
    flat_ranking = {}
    for title, title_ranking in ranking.items():
        for key, value in title_ranking.items():
            if key not in flat_ranking:
                flat_ranking[key] = value
            else:
                flat_ranking[key] += value
    final_ranking = {}
    for key, value in flat_ranking.items():
        final_ranking[key] = 20 - value/20
    return final_ranking


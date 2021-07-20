import requests

default_apikey = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'


class LoLAPI:
    def __init__(self, apikey=default_apikey):
        self.apikey = apikey
        self.host = "https://esports-api.lolesports.com/persisted/gw/"
        self.suffix = "?hl=en-US"

    def get(self, call):
        url = self.host + call + self.suffix
        headers = {
            "Accept": "application/json",
            "x-api-key": self.apikey
        }
        r = requests.get(url, headers=headers).json()
        r.raise_for_status()
        return r

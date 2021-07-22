import requests

from . import session

class LoL:
    def __init__(self, apikey=default_apikey, lang="en-US"):
        self.apikey = apikey
        self.host = "https://esports-api.lolesports.com/persisted/gw/"
        self.lang = lang
        self.suffix = "?hl={}".format(self.lang)

        self.leagues = self.get('getLeagues').get('data').get('leagues')

    def get(self, call):
        url = self.host + call + self.suffix
        headers = {
            "Accept": "application/json",
            "x-api-key": self.apikey
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()

import os
import requests

DEFAULT_APIKEY = os.environ.get('DEFAULT_APIKEY', None)

class LoLget:
    def __init__(self, apikey=DEFAULT_APIKEY, lang="en-US", session=None):
        self.apikey = apikey
        self.host = "https://esports-api.lolesports.com/persisted/gw/"
        self.lang = lang
        self.suffix = "?hl={}".format(self.lang)

        if session:
            self.session = session
        else:
            self.session = requests.Session()
        self.session.params = {'apikey': self.apikey}

    def get(self, call):
        url = self.host + call + self.suffix
        headers = {
            "Accept": "application/json",
            "x-api-key": self.apikey
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.json()

    def get_leagues(self):
        data = self.get('getLeagues')
        return(data.get('data').get('leagues'))

    def get_tournaments(self, tournament_name):
        return []
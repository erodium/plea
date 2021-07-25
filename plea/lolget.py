import requests
from .get_apikey import get_apikey
from .league import League
from .lolresponse import LoLResponse


class LoLget:
    def __init__(self, apikey=get_apikey(), lang="en-US"):
        self.apikey = apikey
        self.host = "https://esports-api.lolesports.com/persisted/gw/"
        self.lang = lang
        self.suffix = "?hl={}".format(self.lang)
        self.headers = {
            "Accept": "application/json",
            "x-api-key": self.apikey
        }

        self.leagues = None
        self.leagues = self._set_leagues()

        for league in self.leagues:
            setattr(type(self), league.get('slug'), League(league))

    def _get(self, call):
        url = self.host + call + self.suffix
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return (LoLResponse(r.status_code, r.json()))

    def _set_leagues(self):
        if not self.leagues:
            response = self._get('getLeagues')
            self.leagues = response.data.get('data').get('leagues')
        return(self.leagues)



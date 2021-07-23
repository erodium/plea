import os
import requests

from .league import League

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

        self.leagues = None

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
        if not self.leagues:
            self.leagues = self.get('getLeagues')
        leagues_list = self.leagues.get('data').get('leagues')
        return(leagues_list)

    def get_league(self, league_id=None):
        if not league_id:
            raise(Exception("Need to specify a league name"))

        for league in self.get_leagues():
            if league_id in [league.get('id'), league.get('name'), league.get('slug')]:
                return(League(league))
        raise(Exception("League name not found"))

    def get_tournaments(self, tournament_name):
        return [{'id':'1', 'slug':'1', 'startDate':'1', 'endDate':'1'}]

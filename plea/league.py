class League:
    def __init__(self, league_info):
        self.id = league_info.get('id')
        self.slug = league_info.get('slug')
        self.name = league_info.get('name')
        self.region = league_info.get('region')

"""
    def getLeague(self, leagueid=None):
        if not leagueid:
            raise(Exception("Need to specify a league name"))

        for league in self.leagues:
            if leagueid.isnumeric():
                if leagueid == league.get('id'):
                    return(League(league))
            elif leagueid in (league.get('name'), league.get('slug')):
                return(League(league))
        raise(Exception("League name not found"))
"""

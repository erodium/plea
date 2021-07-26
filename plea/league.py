from plea import LoLGet

class League:
    def __init__(self, league_info):
        self.id = league_info.get('id')
        self.slug = league_info.get('slug')
        self.name = league_info.get('name')
        self.region = league_info.get('region')


    def list_tournaments(self):
        if not self.tournaments_json:
            self.tournaments_json = self._get_tournaments()
        return(self.tournaments_json)

    def _get_tournaments(self):
        params = {"leagueId": self.id}
        response = self.lol._get('getTournamentsForLeague', params)
        print(response.data)
        return(response.data.get('data').get('leagues')[0].get('tournaments'))

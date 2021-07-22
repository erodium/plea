class League:
    def __init__(self, league_id=None):
        self.id = league_id

        if self.id:
            self.tournaments = self.get_tournaments()



class Tournament:
    def __init__(self, tournament_id=None):
        self.id = tournament_id
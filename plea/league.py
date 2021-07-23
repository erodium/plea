class League:
    def __init__(self, league_info):
        self.id = league_info.get('id')
        self.slug = league_info.get('slug')
        self.name = league_info.get('name')
        self.region = league_info.get('region')

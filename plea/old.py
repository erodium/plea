self.leagues = None

self.leagues_slugs = []
for league_json in self.leagues:
    slug = league_json.get('slug')
    self.leagues_slugs.append(slug)
    setattr(type(self), slug, League(league_json, self))

    def _set_leagues(self):
        if not self.leagues:
            response = self._get('getLeagues')
            self.leagues = response.data.get('data').get('leagues')

    def list_leagues(self):
        if not self.leagues


from plea import League, LoLget, get_apikey
import vcr

APIKEY = get_apikey()
lol = LoLget(APIKEY)

@vcr.use_cassette('tests/vcr/test_league.yaml')
def test_league():
    assert isinstance(lol.lcs, League), "lol should have a league lol.lcs"
    assert isinstance(lol.lcs.id, str), "lol.lcs invalid id"
    assert lol.lcs.id.isnumeric(), "lol.lcs.id should be numeric"
    assert lol.lcs.slug == 'lcs', "lol.lcs.slug wrong"
    assert lol.lcs.name == 'LCS', 'lol.lcs.name wrong'

    t = lol.lcs.list_tournaments()

    assert isinstance(t, list)
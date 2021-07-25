from plea import LoLget, get_apikey
import vcr


APIKEY = get_apikey()
lol = LoLget(APIKEY)

@vcr.use_cassette('tests/vcr/test_lolget.yaml')
def test_lolget():
    assert isinstance(lol, LoLget), "lol should be an instance of LoLget"
    assert isinstance(lol.leagues, list), "leagues should be present as a list"

def test_get_tournaments_for_league():
    pass
    response = lol.get_tournaments_for_league()
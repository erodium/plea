import os
from plea import LoLget
import vcr

DEFAULT_APIKEY = os.environ.get('DEFAULT_APIKEY', None)

@vcr.use_cassette('tests/vcr_cassettes/test_lolget.yaml')
def test_lolget():
    lol = LoLget(DEFAULT_APIKEY)

    leagues_keys = {'id', 'slug', 'name', 'region', 'image', 'priority'}
    leagues = lol.get_leagues()

    assert isinstance(leagues, list), "leagues is not a list"
    assert leagues_keys.issubset(leagues[0].keys()), "All keys should be in the leagues items"

    tournaments_keys = {'id', 'slug', 'startDate', 'endDate'}
    tournaments = lol.get_tournaments('LCS')

    assert isinstance(tournaments, list), "tournaments is not a list"
    assert tournaments_keys.issubset(tournaments[0].keys())
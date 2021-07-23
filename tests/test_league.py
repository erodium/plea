import os
from plea import LoLget, League
import vcr

DEFAULT_APIKEY = os.environ.get('DEFAULT_APIKEY', None)

@vcr.use_cassette('tests/vcr_cassettes/test_league.yaml')
def test_league():
    lol = LoLget(DEFAULT_APIKEY)
    lcs = lol.getLeague('LCS')

    assert isinstance(lcs, League)
    assert lcs.name == "LCS"



import os
from plea import LoLget, League
from pytest import raises
import vcr

DEFAULT_APIKEY = os.environ.get('DEFAULT_APIKEY', None)

@vcr.use_cassette('tests/vcr_cassettes/test_league.yaml')
def test_league():
    lol = LoLget(DEFAULT_APIKEY)
    lcs = lol.get_league('LCS')

    assert isinstance(lcs, League)
    assert lcs.name == "LCS"

    lcs = lol.get_league('lcs')

    assert isinstance(lcs, League)
    assert lcs.name == "LCS"

    lcs = lol.get_league('98767991299243165')

    assert isinstance(lcs, League)
    assert lcs.name == "LCS"

    with raises(Exception) as ex_info:
        lcs = lol.get_league()

    assert ex_info.value.args[0] == "Need to specify a league name"


    with raises(Exception) as ex_info:
        lcs = lol.get_league("fakeleague")

    assert str(ex_info.value) == "League name not found"

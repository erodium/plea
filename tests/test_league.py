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
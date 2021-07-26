from plea import lolget, LoLResponse
import vcr


@vcr.use_cassette('tests/vcr/test_lolget.yaml')
def test_lolget():

    response = lolget('getLeagues')
    assert isinstance(response, LoLResponse), "lol.get should return a LoLResponse"
    assert response.status == 200, "get response failed"
    assert isinstance(response.data, dict), "response not a dict"

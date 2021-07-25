from plea import get_apikey

def test_get_apikey():
    k = get_apikey()

    assert isinstance(k, str)

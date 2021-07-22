# tests/test_plea.py

import os

from plea import APIKeyMissingError
from plea import LoL
import vcr

DEFAULT_APIKEY = os.environ.get('DEFAULT_APIKEY', None)
if not DEFAULT_APIKEY:
     raise APIKeyMissingError

lol = LoL(DEFAULT_APIKEY)

@vcr.use_cassette('test/vcr_cassettes/test_lol.yaml')
def test_lol():
     leagues_keys = {'id', 'slug', 'name', 'region', 'image', 'priority'}
     lol = LoL()
     leagues = lol.leagues

     assert isinstance(leagues, list), "leagues is not a list"
     assert leagues_keys.issubset(leagues[0].keys()),  "All keys should be in the leagues items"


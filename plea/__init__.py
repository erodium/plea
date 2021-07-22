"""Python LoL eSports API wrapper.

PLEA, an acronymn for "Python LoL eSports API" is a python package that allows for
simple access to the LoL eSports API.

More info about PLEA can be found at https://github.com/python-lol-esports-api/plea

"""
import os
import requests

from .lolapi import LoL

DEFAULT_APIKEY = os.environ.get('DEFAULT_APIKEY', None)

class APIKeyMissingError(Exception):
    pass

if not DEFAULT_APIKEY:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "<url>"
        "for how to retrieve an authentication token from"
        "LoL eSports"
    )

session = requests.Session()
session.params = {'apikey':DEFAULT_APIKEY}
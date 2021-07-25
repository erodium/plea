import os

def get_apikey():
    DEFAULT_APIKEY = os.environ.get('DEFAULT_APIKEY', None)
    if not DEFAULT_APIKEY:
        # if no API key provided, use the standard Riot API key
        DEFAULT_APIKEY = "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"
    return DEFAULT_APIKEY


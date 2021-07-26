import requests


class LoLResponse:
    def __init__(self, status=200, data=None):
        self.status = status
        self.data = data


def lolget(call, apikey=None, params=None):
    _apikey = apikey if apikey else "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"
    _host = "https://esports-api.lolesports.com/persisted/gw/"
    _params = {
        "hl": "en-US"
    }
    _headers = {
        "Accept": "application/json",
        "x-api-key": _apikey
    }
    url = _host + call
    p = _params.copy()
    if params:
        p.update(params)
    r = requests.get(url, headers=_headers, params=p)
    print(r.url)
    r.raise_for_status()
    return (LoLResponse(r.status_code, r.json()))
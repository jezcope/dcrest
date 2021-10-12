import requests as rq
from furl import furl

from .endpoints.dois import DOIsEndpoint


class DataCiteClient:
    def __init__(self, test=True, http_client=None):
        if test:
            self._ROOT = furl("https://api.test.datacite.org")
        else:
            self._ROOT = furl("https://api.datacite.org")

        if http_client is None:
            self._http = rq.Session()
        else:
            self._http = http_client

    def get(self, endpoint, *args, **kwargs):
        url = self._ROOT / endpoint
        result = self._http.get(url.url, *args, **kwargs)
        result.raise_for_status()
        return result

    def get_paged(self, endpoint, params, page_size=100):
        url = self._ROOT / endpoint
        final_params = params | {"page[size]": page_size, "page[cursor]": 0}

        result = self._http.get(url.url, params=final_params)
        result.raise_for_status()

        response = result.json()
        yield response

        while "next" in response["links"]:
            result = self._http.get(response["links"]["next"], params=params)
            result.raise_for_status()

            response = result.json()
            yield response

    @property
    def dois(self):
        try:
            return self._dois
        except AttributeError:
            self._dois = DOIsEndpoint(self)
            return self._dois

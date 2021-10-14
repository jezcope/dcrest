import asyncio

import aiohttp
from yarl import URL

from dcrest.endpoints import DOIsEndpoint, ProvidersEndpoint


class DataCiteClient:
    def __init__(self, session, test=True):
        if test:
            self._ROOT = URL("https://api.test.datacite.org")
        else:
            self._ROOT = URL("https://api.datacite.org")

        self._http = session

    async def get(self, endpoint, *args, **kwargs):
        url = self._ROOT / endpoint
        result = await self._http.get(url, *args, **kwargs)
        result.raise_for_status()
        return result

    async def get_paged(self, endpoint, params, page_size=100):
        url = self._ROOT / endpoint
        print(url)
        final_params = params | {"page[size]": page_size, "page[cursor]": 0}

        result = await self._http.get(url, params=final_params)
        result.raise_for_status()

        response = await result.json()
        yield response

        while "next" in response["links"]:
            result = await self._http.get(response["links"]["next"], params=params)
            result.raise_for_status()

            response = await result.json()
            yield response

    @property
    def dois(self):
        try:
            return self._dois
        except AttributeError:
            self._dois = DOIsEndpoint(self)
            return self._dois

    @property
    def providers(self):
        try:
            return self._providers
        except AttributeError:
            self._providers = ProvidersEndpoint(self)
            return self._providers

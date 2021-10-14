from munch import munchify


class ProvidersEndpoint:
    endpoint = "providers"

    def __init__(self, client):
        self._client = client

    async def query(self, params=None):
        if params is None:
            params = {}
        async for page in self._client.get_paged(self.endpoint, params):
            for row in page["data"]:
                yield row

    async def totals(self):
        response = await self._client.get(f"{self.endpoint}/totals")
        result = await response.json()
        return munchify(result)

    async def get(self, provider_id):
        response = await self._client.get(f"{self.endpoint}/{provider_id}")
        result = await response.json()
        return munchify(result["data"])

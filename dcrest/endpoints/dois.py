from munch import munchify


class DOIsEndpoint:
    endpoint = "dois"

    def __init__(self, client):
        self._client = client

    async def query(self, **params):
        async for page in self._client.get_paged(self.endpoint, params):
            for row in page["data"]:
                print("row")
                yield munchify(row)

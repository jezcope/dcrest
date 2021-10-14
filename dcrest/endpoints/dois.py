class DOIsEndpoint:
    endpoint = "dois"

    def __init__(self, client):
        self._client = client

    async def query(self, params=None):
        if params is None:
            params = {}
        async for page in self._client.get_paged(self.endpoint, params):
            for row in page["data"]:
                yield row

class ProvidersEndpoint:
    endpoint = "providers"

    def __init__(self, client):
        self._client = client

    def query(self, params=None):
        if params is None:
            params = {}
        for page in self._client.get_paged(self.endpoint, params):
            yield from page["data"]

    def totals(self):
        result = self._client.get(f"{self.endpoint}/totals")
        return result.json()

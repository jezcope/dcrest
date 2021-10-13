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
        response = self._client.get(f"{self.endpoint}/totals")
        return response.json()

    def get(self, provider_id):
        response = self._client.get(f"{self.endpoint}/{provider_id}")
        result = response.json()
        return result["data"]

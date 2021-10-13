import pytest
from itertools import islice

import dcrest


@pytest.fixture
def client():
    return dcrest.DataCiteClient()


class TestClient:
    def test_has_dois_property(self, client):
        assert hasattr(client, "dois")

    def test_has_providers_property(self, client):
        assert hasattr(client, "providers")


class TestDOIs:
    @pytest.mark.vcr()
    def test_query_simple(self, client):
        rows = client.dois.query()

        for row in islice(rows, 10):
            assert "id" in row
            assert row["type"] == "dois"


class TestProviders:
    @pytest.mark.vcr()
    def test_query_simple(self, client):
        rows = client.providers.query()

        for row in islice(rows, 10):
            assert "id" in row
            assert row["type"] == "providers"

    @pytest.mark.vcr()
    def test_totals_simple(self, client):
        rows = client.providers.totals()

        for row in rows:
            assert "id" in row

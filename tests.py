import pytest

import dcrest


@pytest.fixture
def client():
    return dcrest.DataCiteClient()


class TestClient:
    def test_has_dois_property(self, client):
        dois = client.dois


class TestDOIs:
    @pytest.mark.vcr()
    def test_query_simple(self, client):
        it = client.dois.query()

        row = next(it)
        assert "id" in row
        assert row["type"] == "dois"

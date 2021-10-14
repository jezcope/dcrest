from itertools import islice
from typing import Iterable, Sequence

import aiohttp
import dcrest
import pytest


@pytest.fixture
async def client():
    async with aiohttp.ClientSession() as session:
        yield dcrest.DataCiteClient(session)


class TestClient:
    def test_has_dois_property(self, client):
        assert hasattr(client, "dois")

    def test_has_providers_property(self, client):
        assert hasattr(client, "providers")


@pytest.mark.vcr()
class TestDOIs:
    @pytest.mark.asyncio()
    async def test_query_simple(self, client):
        rows = client.dois.query()

        row = await rows.__anext__()
        print(type(row))
        assert "id" in row
        assert row.type == "dois"


@pytest.mark.vcr()
class TestProviders:
    @pytest.mark.asyncio()
    async def test_query_simple(self, client):
        rows = client.providers.query()

        row = await rows.__anext__()
        assert "id" in row
        assert row.type == "providers"

    @pytest.mark.asyncio()
    async def test_totals_simple(self, client):
        rows = await client.providers.totals()

        for row in rows:
            assert "id" in row
            assert isinstance(row.title, str)

    @pytest.mark.asyncio()
    async def test_get(self, client):
        provider = await client.providers.get("bl")

        assert provider.id == "bl"
        assert provider.type == "providers"

        attrs = provider.attributes
        assert attrs.name == "The British Library"
        assert attrs.country == "GB"
        assert attrs.isActive == True

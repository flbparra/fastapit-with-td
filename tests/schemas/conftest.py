import asyncio
from uuid import UUID
import pytest

from store.db.mongo import db_client
from store.schemas.product import ProductIn
from tests.schemas.factories import product_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_collection_names()

    for collection in collections_names:
        if collection.startswith("system"):
            continue

        await mongo_client.get_database()[collections_names].delete_many({})


@pytest.fixture(scope="function")
def product_id() -> UUID:
    return UUID("e5bde02d-70bd-4690-8c92-2055c5f5bfb8")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)

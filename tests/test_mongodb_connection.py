import pytest
import pymongo
from app.core.config import settings


@pytest.fixture(scope="session")
def test_mongodb_connection():
    client = pymongo.MongoClient(settings.MONGODB_URI)

    result = client.admin.command("ping")
    assert result.get("ok") == 1.0

    yield client
    client.close()


def test_mongodb_fixture(test_mongodb_connection):
    assert test_mongodb_connection.admin.command("ping")["ok"] > 0

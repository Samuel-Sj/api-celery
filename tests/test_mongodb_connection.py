import pytest
import pymongo
from app.core.config import Settings

@pytest.fixture(scope="session")
def test_mongodb_connection():
    # Usando .command() em vez de .connect()
    client = pymongo.MongoClient(Settings.MONGO_URI)
    
    # Testa a conexão com o comando ping do MongoDB
    result = client.admin.command("ping")
    assert result.get("ok") == 1.0

    yield client
    client.close()

def test_mongodb_fixture(test_mongodb_connection):
    assert test_mongodb_connection.admin.command("ping")["ok"] > 0

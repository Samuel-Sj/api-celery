import pytest

pytest_plugins = "celery.contrib.pytest"


@pytest.fixture(scope="session")
def celery_config() -> dict[str, str]:
    return {"broker_url": "redis://localhost:6379/0"}

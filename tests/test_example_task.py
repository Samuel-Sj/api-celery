import pytest
from celery.contrib.testing.worker import start_worker
from app.core.celery_app import celery
from app.tasks.example_task import add

def test_add_tesk_without_redis() -> None:
    assert add(10,20) == 30

@pytest.mark.integration
def test_add_task_with_redis() -> None:
    with start_worker(
        celery, pool="solo", loglevel="info", shutdown_timeout=30, perform_ping_check=False
    ):
        assert add.delay(10,20).get(timeout=10) == 30

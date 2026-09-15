import pytest
from celery.contrib.testing.worker import start_worker
from app.core.celery_app import celery
from app.tasks.add_task import add
from app.tasks.subtract_task import subtract
from app.tasks.division_task import division
from app.tasks.multiply_task import multiply

def test_add_task_without_redis() -> None:
    assert add(10,20) == 30

def test_subtract_task_without_redis() -> None:
    assert subtract(10,5) == 5

def test_multiply_task_without_redis() -> None:
    assert multiply (10,10) == 100

def test_division_task_without_redis() -> None:
    assert division(10,5) == 2

@pytest.mark.xfail
def test_division_with_error() -> None:
    assert division(10,0)


@pytest.mark.integration
def test_add_task_with_redis() -> None:
    with start_worker(
        celery, pool="solo", loglevel="info", shutdown_timeout=30, perform_ping_check=False
    ):
        assert add.delay(10,20).get(timeout=10) == 30

@pytest.mark.integration
def test_subtract_task_with_redis()-> None:
    with start_worker(
        celery, pool="solo", logfile="info", shutdown_timeout=30, perform_ping_check=False
    ):
        assert subtract.delay(10,5).get(timeout=10) == 5

@pytest.mark.integration
def test_multiply_task_with_redis()-> None:
    with start_worker(
        celery, pool="solo", logfile="info", shutdown_timeout=30, perform_ping_check=False
    ):
        assert multiply.delay(10,10).get(timeout=10) == 100

@pytest.mark.integration
def test_division_task_with_redis()-> None:
    with start_worker(
        celery, pool="solo", logfile="info", shutdown_timeout=30, perform_ping_check=False
    ):
        assert division.delay(10,5).get(timeout=10) == 2
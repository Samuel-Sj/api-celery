import time
from app.core.celery_app import celery
from celery.exceptions import TaskError
from loguru import logger


@celery.task(bind=True, max_retries=3)
def multiply(self, x: int, y: int) -> int:
    try:
        logger.info(f"Fazendo {x} x {y}...")
        time.sleep(5)
        return x * y
    except TaskError as taserr:
        logger.error(f"Erro relacionado as tasks: {taserr}")
    except Exception as e:
        raise self.retry(exc=e, countdown=2, **self.request.retries)

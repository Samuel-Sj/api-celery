import time
from app.core.celery_app import celery
from loguru import logger

@celery.task(bind=True,max_retries=3)
def add (self,x:int,y:int):
    try:
        logger.info(f"Fazendo {x} + {y}...")
        time.sleep(5)
        return x + y
    except Exception as e:
        logger.error(f"Erro: {e}")
        raise self.retry(exc=e, countdown=2 ** self.request.retries)
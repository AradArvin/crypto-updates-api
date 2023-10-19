from celery import Task
from celery import shared_task
from .utils import *


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = 2
    retry_jitter=True


@shared_task(bind=True, base=BaseTaskWithRetry)
def async_cryptodata_catcher(self, update_time):
    
    asyncio.run(get_req_data(update_time))
from celery import Celery
import time
import random

app = Celery('simple_task', broker='redis://localhost/', backend= 'redis://localhost/')


@app.task
def wait():
    wait_time = random.random() * 5
    time.sleep(wait_time)
    return "I waited for "+str(wait_time)+" seconds"


@app.task
def greater_than(x, y):
    if x > y:
        return x
    else:
        return y

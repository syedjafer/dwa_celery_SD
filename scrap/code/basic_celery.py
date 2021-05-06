from celery import Celery

app = Celery(
    name = 'tasks',
    broker = 'redis://localhost:6379/0', 
    backend = 'db+sqlite:///db.sqlite3')

import time

@app.task
def absoluteSub(a, b):
	time.sleep(15)
	return abs(a - b)

# celery -A basic_celery worker --loglevel=DEBUG
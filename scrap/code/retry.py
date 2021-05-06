from celery import Celery
app = Celery(
    name = 'tasks',
    broker = 'pyamqp://guest@localhost//', 
    backend = 'db+sqlite:///db.sqlite3')

import time

@app.task(bind=True, max_retries=3)  # you can determine the max_retries here
def errored_func(self):
	try:
		print(1/0)
	except Exception as exc:
		self.retry(exc=exc, countdown=10)
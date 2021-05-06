from celery import Celery
from celery import chain

app = Celery(name="tasks",
			 broker="redis://localhost:6379/0",
			 backend="db+sqlite:///db+sqlite3"
			)

@app.task
def add(x, y):
    return x + y

@app.task
def tsum(numbers):
	return sum(numbers)

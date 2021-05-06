from celery import Celery
app = Celery(
    name = 'tasks',
    broker = 'pyamqp://guest@localhost//', 
    backend = 'db+sqlite:///db.sqlite3')

@app.task
def check():
	print("I am checking your stuff")

app.conf.beat_schedule = {
 "run-me-every-ten-seconds": {
 "task": "task.check",
 "schedule": 10.0
 }
}
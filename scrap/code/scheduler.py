from celery.schedules import crontab
from celery import Celery

app = Celery(
    name = 'tasks',
    broker = 'pyamqp://guest@localhost//', 
    backend = 'db+sqlite:///db.sqlite3')

@app.task
def scheduled_task():
    print("This is a scheduled task")

app.conf.beat_schedule = {
    'add-every-day': {
        'task': 'scheduler.scheduled_task',
        'schedule': crontab(hour=15, minute=21),
    },
}
app.conf.timezone = 'Asia/Kolkata'

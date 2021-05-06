from celery import Celery
import time
from celery.schedules import crontab

app = Celery(name="tasks",
			 broker="redis://localhost:6379/0",
			 backend="db+sqlite:///db+sqlite3"
			)

# Simple Task run
# @app.task
# def absoluteSub(a, b):
# 	time.sleep(15)
# 	return abs(a - b)

# scheduled task
# @app.task
# def scheduled_task():
#     print("This is a scheduled task")


# app.conf.beat_schedule = {
#     'add-every-day': {
#         'task': 'tasks.scheduled_task',
#         'schedule': crontab(hour=20, minute=50),
#     },
# }
# app.conf.timezone = 'Asia/Kolkata'

# For Every y seconds:
# @app.task
# def check():
# 	print("I am checking your stuff")

# app.conf.beat_schedule = {
#  "run-me-every-ten-seconds": {
#  "task": "tasks.check",
#  "schedule": 10.0
#  }
# }


@app.task
def add(data):
	time.sleep(15)
	return data[0]+data[1]

@app.task
def tsum(numbers):
    return sum(numbers)


#result = add.apply_async(args=[[4, 6]], queue='low-priority)
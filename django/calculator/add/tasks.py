from celery import shared_task
from time import sleep

@shared_task
def add_func(param1, param2):
	sleep(10)
	return param2+param1
from django.shortcuts import render
from django.http import HttpResponse
from add.tasks import add_func
from celery.result import AsyncResult

# Create your views here.
def add(request, param1, param2):
	res = add_func.delay(param1, param2)
	return HttpResponse(str(res))

def result(request, async_key):
	res = AsyncResult(async_key)
	if res.status:
		return HttpResponse(str(res.get()))
	else:
		return HttpResponse(res.status)
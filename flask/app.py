from celery import Celery
from celery.result import AsyncResult

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    # class ContextTask(celery.Task):
    #     def __call__(self, *args, **kwargs):
    #         with app.app_context():
    #             return self.run(*args, **kwargs)

    # celery.Task = ContextTask
    return celery

from flask import Flask

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='db+sqlite:///db+sqlite3'
)
celeryy = make_celery(flask_app)

@celeryy.task()
def add_together(a, b):
    return a + b

@flask_app.route('/add/<int:param1>/<int:param2>')
def add(param1, param2):
    r = add_together.delay(param1, param2)
    return str(r)


@flask_app.route('/result/<string:async_key>')
def get_result(async_key):

    print(async_key)
    r = celeryy.AsyncResult(str(async_key))
    # print(r, r.status)
    if r.ready:
        return str(r.get())
    else:
        return r.status

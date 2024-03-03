from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('netology_pd_diplom_3')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def sort_iter(data):
    return sorted(data)


@app.task
def get_sum(data):
    return sum(data)

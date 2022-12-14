import os
from celery import Celery
from celery.schedules import crontab
from celery import app as celery_app
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')
 
app = Celery('newspaper')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'when_creating_post': {
        'task': 'printscreen',
        'schedule': 30,
        'args': ("some_arg"),
    },
}

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'action',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': ("some_arg"),
    },
}
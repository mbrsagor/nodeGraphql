import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taskschedule.settings')

app = Celery('Taskschedule')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.update(result_expires=3600, enable_utc=True, timezone='Asia/Dhaka', )

app.conf.beat_schedule = {
    'schedule-everyday-1-hours': {
        'task': 'entry.tasks.create_schedule',
        'schedule': 3600.0,  # Every 1 hours
        'args': ('test day task schedule',)
    },
}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

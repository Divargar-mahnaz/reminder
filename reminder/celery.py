import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reminder.settings')

app = Celery('reminder')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Asia/Tehran'

app.conf.beat_schedule = {
    # Scheduler Name
    'today_remember': {
        # Task Name (Name Specified in Decorator)
        'task': 'Today_reminders',
        # Schedule
        'schedule': crontab(hour=0, minute=0),

    },
}

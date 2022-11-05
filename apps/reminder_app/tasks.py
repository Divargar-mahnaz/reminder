from django.utils import timezone
import datetime
from reminder import celery_app
from reminder.settings import QUEUE, DEFAULT_FROM_EMAIL
from .models.reminder import Reminder

from django.core.mail import send_mail


@celery_app.task(queue=QUEUE, name='Today_reminders')
def today_remember():
    """
    send email to tell user ,how set reminder for today.
    """
    for task in Reminder.objects.filter(expired=False):
        if task.remember_time == datetime.datetime.now().date():
            send_mail(
                task.name,
                task.description,
                DEFAULT_FROM_EMAIL,
                [str(task.user.email)],
                fail_silently=False,
            )


@celery_app.task(queue=QUEUE, name='remind')
def remind(reminder_id):
    """
    send email to tell user ,for do task and set it as expired.
    """
    reminder = Reminder.objects.get_object(pk=reminder_id)
    send_mail(
        reminder.name,
        reminder.description,
        DEFAULT_FROM_EMAIL,
        [str(reminder.user.email)],
        fail_silently=False,
    )
    reminder.expire()

import time

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from reminder import celery_app
from .models.reminder import Reminder
from .tasks import remind


# @receiver(pre_save, sender=Reminder)
# def delete_previous_task(sender, instance, **kwargs):
#     if instance.id:
#         previous = Reminder.objects.get_object(id=instance.id)
#         if previous.datetime != instance.datetime:  # datetime changed.
#             print('change time, then delete previous task')
#             task_id = 'task_for_remind_to_user_{}'.format(instance.id)
#             celery_app.control.revoke(task_id, terminate=True)


@receiver(post_save, sender=Reminder)
def creare_task(sender, instance, created, **kwargs):
    task_id = 'task_for_remind_to_user_{}'.format(instance.id)
    if not instance.expired:
        remind.apply_async(kwargs={'reminder_id': instance.id},
                           task_id=task_id,
                           eta=instance.datetime)

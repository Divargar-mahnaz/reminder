import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from apps.reminder_app.exceptions import InvalidThreshold, InvalidDateTime
from apps.reminder_app.manager import ReminderManager
from common.base_model import BaseModel
from common.validators import check_threshold


class Reminder(BaseModel):
    user = models.ForeignKey(User, related_name='Reminders', on_delete=models.CASCADE)
    name = models.CharField('Reminder Name', max_length=50)
    description = models.TextField('Description')
    threshold = models.PositiveSmallIntegerField('Threshold', null=True, validators=[check_threshold])
    datetime = models.DateTimeField('Datetime')
    expired = models.BooleanField(default=False)
    objects = ReminderManager()

    def __str__(self):
        return self.name + str(self.datetime)

    @property
    def remember_time(self):
        return (self.datetime - datetime.timedelta(days=self.threshold)).date()

    def expire(self):
        self.expired = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.expired:
            if self.datetime < timezone.now():
                raise InvalidDateTime
            if self.threshold and self.remember_time <= datetime.datetime.now().date():
                raise InvalidThreshold
        super(Reminder, self).save(*args, **kwargs)

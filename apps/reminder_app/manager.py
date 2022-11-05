from django.db import models
from django.core.exceptions import ValidationError
from common.messages import NOT_FOUNT


class ReminderManager(models.Manager):
    def get_object(self,  **keyword):
        try:
            return self.get(**keyword)
        except (self.model.DoesNotExist, ValidationError):
            raise NOT_FOUNT

from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission

from apps.reminder_app.models import Reminder


#
class OwnerPermission(BasePermission):
    message = _("access denied")

    def has_permission(self, request, view):
        print('check perm')
        pk = view.kwargs['pk']
        reminder = Reminder.objects.get_object(pk=pk)
        return request.user.id == reminder.user.id

from common.base_view import ListCreateView, RetrieveUpdateDestroyView
from reminder import celery_app
from .models import Reminder
from .serializer.reminder import ReminderGetSerializer, ReminderPostSerializer


class ReminderListCreateApiView(ListCreateView):
    queryset = Reminder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user__id=self.request.user.id)

    def get_serializer_class(self, ):
        if self.request.method == 'GET':
            return ReminderGetSerializer
        return ReminderPostSerializer


class ReminderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderGetSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        task_id = 'task_for_remind_to_user_{}'.format(instance.id)
        celery_app.control.revoke(task_id, terminate=True)
        return self.destroy(request, *args, **kwargs)

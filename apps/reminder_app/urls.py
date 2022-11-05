from django.urls import path

from .views import ReminderListCreateApiView, ReminderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ReminderListCreateApiView.as_view(), name='reminder_list_create'),
    path('<int:pk>/', ReminderRetrieveUpdateDestroyAPIView.as_view(), name='reminder_retrieve_update_destroy')
]

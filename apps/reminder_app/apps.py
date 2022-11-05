from django.apps import AppConfig


class ReminderAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.reminder_app'

    def ready(self):
        import apps.reminder_app.signals

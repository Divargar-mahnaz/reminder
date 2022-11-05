from apps.reminder_app.exceptions import InvalidThreshold


def check_threshold(threshold):
    if threshold <= 0:
        raise InvalidThreshold

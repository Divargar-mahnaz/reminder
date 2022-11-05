from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidThreshold(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "آستانه وارد شده نامعتبر است."
    default_code = "INVALID_THRESHOLD"


class InvalidDateTime(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "تاریخ وارد شده، نامعتبر است."
    default_code = "INVALID_DateTime"

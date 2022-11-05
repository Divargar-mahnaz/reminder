from rest_framework import status
from rest_framework.exceptions import APIException


class LoginFail(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "کاربری با این مشخصات یافت نشد."
    default_code = "INVALID_USER_INFO"

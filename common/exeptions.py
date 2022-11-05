from rest_framework import status
from rest_framework.exceptions import APIException
from .messages import NOT_FOUNT

class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = NOT_FOUNT
    default_code = "NOT_FOUNT"

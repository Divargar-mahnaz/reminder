from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response as JsonResponse
from rest_framework import status


class Response(JsonResponse):
    detail_msg = _("mission accomplished")
    code_msg = status.HTTP_200_OK

    def __init__(self, data=[], detail=detail_msg, code=code_msg, **kwargs):
        super(Response, self).__init__({"data": data, "detail": detail, "code": code}, **kwargs)


class ExceptionResponse(JsonResponse):
    detail_msg = _("mission accomplished")

    def __init__(self, data=None, detail=detail_msg, code=_("BAD_REQUEST"), **kwargs):
        response = {
            "data": data,
            "detail": detail,
            "code": code
        }
        super(ExceptionResponse, self).__init__(response, **kwargs)

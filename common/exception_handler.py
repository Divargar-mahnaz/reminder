from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from rest_framework import status
from rest_framework.views import set_rollback

from common.response import ExceptionResponse


def custom_exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    if isinstance(exc, exceptions.APIException):
        headers = {}
        code = getattr(exc, 'default_code', None)
        set_rollback()
        error_detail = dict()
        for item in exc.detail:
            try:
                error_detail[item] = exc.detail[item]
            except (AttributeError, TypeError):
                error_detail = exc.detail
            except KeyError:
                error_detail[item] = exc.detail[item]

        return ExceptionResponse(data=None, detail=error_detail, code=code, status=exc.status_code, headers=headers)
    elif isinstance(exc, Http404):
        msg = _('Not found.')
        set_rollback()
        return ExceptionResponse(detail=msg, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        set_rollback()
        return ExceptionResponse(detail=str(msg), status=status.HTTP_403_FORBIDDEN)

    return None

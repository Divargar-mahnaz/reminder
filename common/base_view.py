from django.db import transaction
from django.http.request import QueryDict
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.views import APIView

from common.permission import OwnerPermission


class NoAuthAPIView(APIView):
    """
    non user  view
    """
    permission_classes = (BasePermission,)


class ListCreateView(ListCreateAPIView):
    """
    all users view
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            # if user use form data for enter data, type of request.data is QueryDict and is immutable.
            request.data._mutable = True
        request.data['user'] = request.user.pk
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    all users view
    """
    permission_classes = (IsAuthenticated, OwnerPermission)

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

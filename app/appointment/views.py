from appointment import serializers
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

from core import models


class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Base viewset for appointments atributes"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        assigned_only = bool(
            int(self.request.query_params.get('assigned_only', 0))
        )
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(appointment_scheduling__isnull=False)

        return queryset.filter(
            user=self.request.user
        ).order_by('-day').distinct()



class AppointmentSchedulingViewSet(BaseRecipeAttrViewSet):
    """Manage appointment in the database"""
    queryset = models.AppointmentScheduling.objects.all().order_by(
        'day',
        'hour'
    ).filter(day__gte=datetime.now())
    serializer_class = serializers.AppointmentSchedulingSerializer

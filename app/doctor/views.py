from doctor import serializers
from django.shortcuts import render
from rest_framework import mixins, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime
from django_filters import rest_framework as filters_complex

from core import models


class BaseAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Base viewset for user doctor, medical specialty and appointments atributes
    """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class MedicalSpecialtyViewSet(BaseAttrViewSet):
    """Manage medical specialty in the database"""
    queryset = models.MedicalSpecialty.objects.all()
    serializer_class = serializers.MedicalSpecialtySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['specialty']


class DoctorFilter(filters_complex.FilterSet):
    search = filters_complex.CharFilter(
        field_name='name', lookup_expr='icontains', label='Doctor')
    specialty = filters_complex.ModelMultipleChoiceFilter(
        field_name='specialty',
        to_field_name='id',
        queryset=models.MedicalSpecialty.objects.all(),
    )

    class Meta:
        model = models.Doctor
        fields = ['search', 'specialty']


class DoctorViewSet(BaseAttrViewSet):
    """Manage doctor in the database"""
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DoctorFilter


class AppointmentSchedulingViewSet(viewsets.GenericViewSet,
                                   mixins.ListModelMixin):
    """Manage appointment in the database"""
    queryset = models.AppointmentScheduling.objects.all().order_by(
        'day',
        'hour'
    ).filter(day__gte=datetime.now())
    serializer_class = serializers.AppointmentSchedulingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the appointment for the authenticated user"""
        doctors = self.request.query_params.get('doctor')
        queryset = self.queryset
        if doctors:
            doctor_ids = self._params_to_ints(doctors)
            queryset = queryset.filter(doctors__id__in=doctor_ids)

        return queryset.filter(user=self.request.user)


class ScheduleFilter(filters_complex.FilterSet):
    day_after = filters_complex.DateFilter(
        field_name="day", lookup_expr='gte', label='Day After')
    day_before = filters_complex.DateFilter(
        field_name="day", lookup_expr='lte', label='Day Before')
    doctor = filters_complex.ModelMultipleChoiceFilter(
        field_name='doctor',
        to_field_name='id',
        queryset=models.Doctor.objects.all(),
    )
    specialty = filters_complex.ModelMultipleChoiceFilter(
        field_name='specialty',
        to_field_name='id',
        queryset=models.MedicalSpecialty.objects.all(),
    )

    class Meta:
        model = models.AvailableSchedule
        fields = ['doctor', 'specialty', 'day_after', 'day_before']


class AvailableScheduleViewSet(BaseAttrViewSet):
    """Manage available schedule in the database"""
    queryset = models.AvailableSchedule.objects.all().order_by('-day')
    serializer_class = serializers.AvailableScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctor']
    filterset_class = ScheduleFilter

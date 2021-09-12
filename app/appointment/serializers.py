from rest_framework import serializers

from core.models import AppointmentScheduling
from doctor.serializers import DoctorSerializer


class AppointmentSchedulingSerializer(serializers.ModelSerializer):
    """Serializer for appointment objects"""
    doctor = DoctorSerializer()

    class Meta:
        model = AppointmentScheduling
        fields = ['id', 'day', 'hour', 'scheduling_date', 'doctor']

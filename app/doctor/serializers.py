from rest_framework import serializers

from core.models import (
    Doctor,
    MedicalSpecialty, 
    AppointmentScheduling,
    AvailableSchedule,
    Hour
)


class MedicalSpecialtySerializer(serializers.ModelSerializer):
    """Serializer for medical specialty objects"""

    class Meta:
        model = MedicalSpecialty
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer for doctor objects"""
    specialty = MedicalSpecialtySerializer()

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'crm', 'email', 'phone_number', 'specialty']


class AppointmentSchedulingSerializer(serializers.ModelSerializer):
    """Serializer for appointment objects"""
    doctor = DoctorSerializer()

    class Meta:
        model = AppointmentScheduling
        fields = ['id', 'day', 'hour', 'scheduling_date', 'doctor']


class HourSerializer(serializers.RelatedField):
    def to_representation(self, value):
        hour = value.hour.strftime("%H:%M")
        return '%s' % hour 


class AvailableScheduleSerializer(serializers.ModelSerializer):
    """Serializer for available schedule objects"""
    doctor = DoctorSerializer()
    hour = HourSerializer(many=True, read_only=True)

    class Meta:
        model = AvailableSchedule
        fields = ['id', 'doctor', 'day', 'hour']

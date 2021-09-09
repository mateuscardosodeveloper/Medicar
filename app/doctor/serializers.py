from django.db.models.query import QuerySet
from rest_framework import serializers

from core.models import Doctor, MedicalSpecialty


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

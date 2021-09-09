from doctor import serializers
from django.shortcuts import render
from rest_framework import mixins, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from core import models


class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Base viewset for user doctor and medical specialty atributes"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class MedicalSpecialtyViewSet(BaseRecipeAttrViewSet):
    """Manage medical specialty in the database"""
    queryset = models.MedicalSpecialty.objects.all()
    serializer_class = serializers.MedicalSpecialtySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['specialty']


class DoctorViewSet(BaseRecipeAttrViewSet):
    """Manage doctor in the database"""
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['specialty']

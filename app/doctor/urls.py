from django.urls import path, include
from rest_framework.routers import DefaultRouter

from doctor import views

router = DefaultRouter()
router.register('medical_specialty', views.MedicalSpecialtyViewSet)
router.register('doctor', views.DoctorViewSet)
app_name = 'doctor'

urlpatterns = [
    path('', include(router.urls))
]

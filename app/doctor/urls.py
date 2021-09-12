from django.urls import path, include
from rest_framework.routers import DefaultRouter

from doctor import views
from appointment.views import AppointmentSchedulingViewSet

router = DefaultRouter()
router.register('medical_specialty', views.MedicalSpecialtyViewSet)
router.register('doctor', views.DoctorViewSet)
router.register('appointment', AppointmentSchedulingViewSet)
app_name = 'doctor'

urlpatterns = [
    path('', include(router.urls))
]

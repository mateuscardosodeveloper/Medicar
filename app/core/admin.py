from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Import dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class AppointmentSchedulingAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'hour', 'scheduling_date']


class AvailableScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'doctor', 'hours']

admin.site.register(models.User, UserAdmin)
admin.site.register(models.MedicalSpecialty)
admin.site.register(models.Doctor)
admin.site.register(models.Hour)
admin.site.register(models.AvailableSchedule, AvailableScheduleAdmin)
admin.site.register(models.AppointmentScheduling, AppointmentSchedulingAdmin)

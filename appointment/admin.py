from django.contrib import admin
from . import models
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['doctor_name', 'name' ,'time', 'date',] 
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
admin.site.register(models.Appointment, AppointmentAdmin)
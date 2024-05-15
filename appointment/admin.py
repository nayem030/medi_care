from django.contrib import admin
from . import models
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['doctor', 'name' ,'time', 'date',] 
    
admin.site.register(models.Appointment, AppointmentAdmin)
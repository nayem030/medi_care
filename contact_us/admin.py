from django.contrib import admin
from . import models

class ContactUsAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'subject', 'massage']
    
admin.site.register(models.ContactUs, ContactUsAdmin)

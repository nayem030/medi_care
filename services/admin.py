from django.contrib import admin
from services.models import Services

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display=['name', 'image']
    

admin.site.register(Services, ServicesAdmin)

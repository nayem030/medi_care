from django.db import models

class Services(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to="services/images/")
    
    class Meta:
        verbose_name_plural = "services"

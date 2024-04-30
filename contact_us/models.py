from django.db import models

class ContactUs(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=250)
    subject=models.CharField(max_length=100)
    massage=models.TextField()
    
    class Meta:
        verbose_name_plural = 'contact_us'

from django.db import models

class MedicalPackage(models.Model):
    name=models.CharField(max_length=50)
    descriptions=models.TextField()
    image=models.ImageField(upload_to="medical_package/images/")
    fee=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.name

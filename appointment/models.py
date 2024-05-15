from django.db import models
from doctor.models import Doctor, Department
from patient.models import Patient
# Create your models here.

class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    doctor= models.OneToOneField(Doctor, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} Patient: {self.name}"
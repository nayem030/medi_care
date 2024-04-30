from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

class Department(models.Model):
    name=models.CharField(max_length=50)
    slug= models.SlugField(max_length=50)
    
    def __str__(self):
        return self.name

class Specialization(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    
    def __str__(self):
        return self.name

class Designation(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="doctor/images/")
    designation=models.ManyToManyField(Designation)
    specialization=models.ManyToManyField(Specialization)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    fee=models.IntegerField()
    time =models.CharField(max_length=100)
    meet_link=models.CharField(max_length=200)
    
    def __str__(self):
        return f" Dr. {self.user.first_name} {self.user.last_name}"
    
    
class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    body=models.TextField()
    
   
    

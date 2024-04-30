from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class =serializers.DoctorSerializers
    
class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class =serializers.DesignationSerializers

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class =serializers.SpecializationSerializers
    
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class =serializers.DepartmentSerializers
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class =serializers.ReviewSerializers
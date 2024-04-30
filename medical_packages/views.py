from django.shortcuts import render
from  rest_framework import viewsets
from .import models
from . import serializers

class MedicalPackageViewSet(viewsets.ModelViewSet):
    queryset= models.MedicalPackage.objects.all()
    serializer_class = serializers.MediaclPackageSerializer
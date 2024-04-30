from django.shortcuts import render
from . import models , serializers
from rest_framework import viewsets
# Create your views here.

class ContactUsViewset(viewsets.ModelViewSet):
    queryset=models.ContactUs.objects.all()
    serializer_class=serializers.ContactUsSerializers
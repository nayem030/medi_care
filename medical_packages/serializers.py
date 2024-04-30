from rest_framework import serializers
from . import models

class MediaclPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalPackage
        fields= '__all__'
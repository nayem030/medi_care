from rest_framework import serializers
from .import models

class AppointmentSerializers(serializers.ModelSerializer):
    department= serializers.StringRelatedField(many=True)
    doctor= serializers.StringRelatedField(many=True)
    class Meta:
        model=models.Appointment
        fields ='__all__'
from rest_framework import serializers
from .import models

class AppointmentSerializers(serializers.ModelSerializer):
    department= serializers.StringRelatedField(many=False)
    doctor= serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Appointment
        fields ='__all__'
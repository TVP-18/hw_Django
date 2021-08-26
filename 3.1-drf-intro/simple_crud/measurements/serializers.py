from rest_framework import serializers
from .models import Project, Measurement


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at']


class MeasurementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'value', 'project', 'image', 'created_at', 'updated_at']

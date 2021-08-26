from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectModelSerializer, MeasurementModelSerializer
from .models import Project, Measurement


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementModelSerializer

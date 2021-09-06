# from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrAdmin
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    # фильтры по creator, status, create_at
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        # if self.action in ["create", "update", "partial_update"]:
        #     return [IsAuthenticated()]

        # создать объявление может зарегистрированный пользователь
        if self.action in ["create"]:
            return [IsAuthenticated()]

        # обновить, удалить объявление только владелец
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]

        return []

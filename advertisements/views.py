from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    serializer_class = AdvertisementSerializer

    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        queryset = Advertisement.objects.all().exclude(status='DRAFT')

        if self.request.user.is_active:
            user = self.request.user
            queryset = Advertisement.objects.all().exclude(status='DRAFT') | Advertisement.objects.all().filter(status='DRAFT').filter(creator=user)

        return queryset

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == 'create':
            return [IsAuthenticated()]

        if self.action in ['destroy', 'update', 'partial_update']:
            return [IsOwner()]
        return []

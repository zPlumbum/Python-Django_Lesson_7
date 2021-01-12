from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    id = filters.ModelMultipleChoiceFilter(
        queryset=Advertisement.objects.all(),
        field_name='id',
        to_field_name='id'
    )
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['id', 'created_at', 'status']

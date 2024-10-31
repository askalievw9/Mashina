from django.template.defaultfilters import title
from django_filters import FilterSet
from .models import Car


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'marka': ['exact'],
            'year': ['exact'],
            'title': ['exact'],
            'price': ['gt', 'lt']


        }
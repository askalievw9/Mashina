from rest_framework import serializers
from .models import *


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = ['marka_name']

class CarSerializer(serializers.ModelSerializer):
    marka = MarkaSerializer()
    class Meta:
        model = Car
        fields = ['title', 'description', 'marka', 'price', 'color',
                  'volume', 'year', 'type_change', 'image', 'video']
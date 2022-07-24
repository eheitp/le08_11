from rest_framework import serializers
from .models import Dht

# Serializers define the API representation.
class Dhser(serializers.ModelSerializer):
    class Meta:
        model = Dht
        fields = ['id', 'temp','hum','dt']
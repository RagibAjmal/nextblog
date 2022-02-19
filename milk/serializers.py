from rest_framework import serializers
from .models import year2022


class Month(serializers.ModelSerializer):
    class Meta:
        model = year2022
        fields = ['Jan']

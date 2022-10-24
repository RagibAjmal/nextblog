from rest_framework import serializers
from .models import Item, Cart


class itemIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'getImage', 'id', 'ratings']


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'price', 'getImage', 'id', 'ratings']


class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'ratings', 'price', 'getImage', 'id']

from django.shortcuts import render


from .models import Item
from .serializers import itemSerializer
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import JsonResponse


# Create your views here.
class Items(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id, format=None):
        print(request)
        item = Item.objects.get(id=id)
        serializer = itemSerializer(item)
        return JsonResponse(serializer.data, safe=False)

from lib2to3.pgen2 import token
from sre_constants import SUCCESS
from telnetlib import AUTHENTICATION
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

from .serializers import Month
from .models import year2022
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.views import APIView
from rest_framework import permissions


class sample(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user_num = str(request.user).split()[1]
        a = year2022.objects.get(user=user_num)
        serializer = Month(a)
        return JsonResponse(serializer.data, safe=False)

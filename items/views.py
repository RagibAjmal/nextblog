from django.shortcuts import render


from .models import Item, Cart
from .serializers import itemSerializer, itemIdSerializer, cartSerializer
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import JsonResponse
from auth_user.models import CustomUser as User
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class ItemsId(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id, format=None):

        item = Item.objects.get(id=id)
        serializer = itemIdSerializer(item)
        return JsonResponse(serializer.data, safe=False)


class Items(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, start, end, format=None):

        item = Item.objects.all()[start:end]
        serializer = itemSerializer(item, many=True)
        return JsonResponse(serializer.data, safe=False)


class cart_add(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id, format=None):
        simple_jwt = JWTAuthentication()
        user_object = simple_jwt.authenticate(request)[0]
        user = User.objects.get(email=user_object)
        if Cart.objects.filter(user=user).exists():
            cart = Cart.objects.get(user=user)

        else:
            cart = Cart.objects.create(user=user)

        item = Item.objects.get(id=id)

        cart.cart[id] = 1
        cart.save()
        return JsonResponse({"success": True}, safe=False)


class item_clear(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id, format=None):
        simple_jwt = JWTAuthentication()
        user_object = simple_jwt.authenticate(request)[0]
        user = User.objects.get(email=user_object)
        cart = Cart.objects.get(user=user)
        cart.cart.pop(str(id))
        cart.save()
        return JsonResponse("success", safe=False)


class item_increment(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id, format=None):
        simple_jwt = JWTAuthentication()
        user_object = simple_jwt.authenticate(request)[0]
        user = User.objects.get(email=user_object)
        cart = Cart.objects.get(user=user)
        cart.cart[str(id)] += 1
        cart.save()
        return JsonResponse("success", safe=False)


class item_decrement(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id, format=None):
        simple_jwt = JWTAuthentication()
        user_object = simple_jwt.authenticate(request)[0]
        user = User.objects.get(email=user_object)
        cart = Cart.objects.get(user=user)
        if cart.cart[str(id)] != 1:
            cart.cart[str(id)] -= 1
        else:
            cart.cart.pop(str(id))
        cart.save()
        return JsonResponse("success", safe=False)


class cart_clear(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,  format=None):
        simple_jwt = JWTAuthentication()
        user_object = simple_jwt.authenticate(request)[0]
        user = User.objects.get(email=user_object)
        cart = Cart.objects.get(user=user)
        cart.cart = dict()
        cart.save()
        return JsonResponse("success", safe=False)


class cart_items(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,  format=None):
        simple_jwt = JWTAuthentication()
        user_object = simple_jwt.authenticate(request)[0]
        user = User.objects.get(email=user_object)
        cart = Cart.objects.get(user=user)
        cart_keys = cart.cart.keys()
        cart_item = Item.objects.filter(id__in=cart_keys)
        serializer = cartSerializer(cart_item, many=True)
        for i in serializer.data:
            i['quantity'] = cart.cart[str(i['id'])]
        return JsonResponse(serializer.data, safe=False)

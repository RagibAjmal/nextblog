from django.http import HttpResponse
import json
from . models import CustomUser as User
from nextblog import settings
from django.core.mail import send_mail, EmailMessage
from . tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.views import APIView
from rest_framework import permissions
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
# Create your views here.


class signup(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        # Get the JSON from the request body
        data = request.body.decode('utf-8')
        data = json.loads(data)

        # Get the username and password from the JSON
        if User.objects.filter(email=data['email']).exists():
            return HttpResponse('email already exists')

        user = User.objects.create_user(email=data["email"], password=data["password"],
                                        first_name=data["first_name"], last_name=data["last_name"],  is_active=False)
        user.save()

        # Welcome Email
        subject = "Welcome to Aruvadai Organic Store !!"
        message = "Hello " + user.first_name + "!! \n" + \
            "Welcome to Aruvadai Organic Store!! \nThank you for visiting our website.\nWe have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nRagib Ajmal"
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @  Aruvadai Organic Store Login!!"
        message2 = render_to_string('email_confirmation.html', {

            'name': user.first_name,
            'domain': config('DOMAIN'),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.fail_silently = True
        email.send()
        return HttpResponse('ok')


class activate(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Your email has been confirmed.')
        else:
            return HttpResponse('Error')


class user_details(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        simple_jwt = JWTAuthentication()
        user = simple_jwt.authenticate(request)[0]
        user_object = User.objects.get(email=user)
        return HttpResponse(json.dumps({"first_name": user_object.first_name, "last_name": user_object.last_name, "email": user_object.email}))


class OAuth(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, provider):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        if provider == "google":
            profile_url = "https://www.googleapis.com/oauth2/v1/userinfo"
            resp = requests.get(
                profile_url,
                params={
                    "access_token": data["access_token"], "alt": "json"},
            )
            resp.raise_for_status()
            OAuth_data = resp.json()
            email = OAuth_data["email"]
            first_name = OAuth_data["name"]
        elif provider == "github":
            profile_url = "https://api.github.com/user"
            headers = {"Authorization": "token {}".format(
                data["access_token"])}
            resp = requests.get(profile_url+"/emails", headers=headers)
            resp.raise_for_status()
            OAuth_data = resp.json()
            resp_user_data = requests.get(profile_url, headers=headers)
            resp_user_data.raise_for_status()
            OAuth_user_data = resp_user_data.json()
            email = OAuth_data[0]["email"]
            first_name = OAuth_user_data["name"]

        user_object = User.objects.filter(email=email)

        if (user_object.exists()):
            user_object = User.objects.get(email=email)
        else:
            password = User.objects.make_random_password()
            user_object = User.objects.create_user(
                email=email, first_name=first_name, password=password, is_active=True)
            user_object.save()

        refresh = RefreshToken.for_user(user_object)

        refresh_token = str(refresh),
        access_token = str(refresh.access_token),
        user_data = {"first_name": user_object.first_name,
                     "email": user_object.email}

        return HttpResponse(json.dumps({"refresh_token": refresh_token[0], "access_token": access_token[0], "userData": user_data}))


class forgotPassword(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        user_object = User.objects.filter(email=data["email"])
        if not (user_object.exists()):
            return HttpResponse('User does not exist')
        user_object = User.objects.get(email=data["email"])
        email_subject = "Reset Password @  Aruvadai Organic Store!!"
        message2 = render_to_string('forgotPassword.html', {

            'name': user_object.first_name,
            'domain': config('DOMAIN'),
            'uid': urlsafe_base64_encode(force_bytes(user_object.pk)),
            'token': generate_token.make_token(user_object)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user_object.email],
        )
        email.fail_silently = True
        email.send()
        return HttpResponse('Email sent successfully to '+user_object.email+' Please check your email to reset your password')


class resetPassword(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, uidb64, token):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.set_password(data["password"])
            user.save()
            return HttpResponse('Password has been changed successfully!!')
        else:
            return HttpResponse('Error')

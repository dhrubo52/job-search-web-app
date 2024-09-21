import re
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIViews
from rest_framework.response import Response
from rest_framework import status
from allmodels import UserProfile

# Create your views here.

def valid_email(email):
    e = re.match('[a-z0-9]+([-._][a-z0-9]+)*@[a-z0-9]+([-][a-z0-9]+)*([.]..+)+', email)

class Register(APIView):
    def post(self, request):
        email = request.data['email']
        password1 = request.data['password1']
        password2 = request.data['password2']
        first_name = request.data('first_name')
        last_name = request.data('last_name')
        profile_type = request.data['profile_type']

        if User.objects.get(email=email, None):
            return Response({message: 'A user with this email address already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if password1 != password2:
            return Response({message: 'Both password have to be same.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.obejects.create(email=email, password=make_password(password1), first_name=first_name, last_name=last_name)
        UserProflie.objects.create(user=user, profile_type=profile_type)


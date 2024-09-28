import re
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from allmodels.models import UserProfile
from .forms import UserRegistrationForm

# Create your views here.

def valid_email(email):
    e = re.match('[a-z0-9]+([-._][a-z0-9]+)*@[a-z0-9]+([-][a-z0-9]+)*([.]..+)+', email)
    if e is not None:
        return True
    else: 
        return False

class Register(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        password1 = request.data.get('password1', '')
        password2 = request.data.get('password2', '')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        profile_type = request.data.get('profile_type', '')

        if User.objects.filter(email=email).exists():
            return Response({'message': 'A user with this email address already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        if password1 != password2:
            return Response({'message': 'Both passwords have to be same.'}, status=status.HTTP_400_BAD_REQUEST)

        user_data = {
            'email': email,
            'password': password1,
            'first_name': first_name,
            'last_name': last_name
        }
        user_form = UserRegistrationForm(user_data)

        try:
            if user_form.is_valid():
                print('form is valid')
            else:
                print(dir(user_form.errors))
                for i in user_form.errors.items():
                    print(i[1][0])
        except Exception as e:
            print(e)
            

        # try:
        #     validate_password(password1)
        # except Exception as e:
        #     print(e)

        # print(make_password(password1))

        # user = User.obejects.create(email=email, password=password, first_name=first_name, last_name=last_name)
        # UserProfile.objects.create(user=user, profile_type=profile_type)

        return Response({'message': 'Registration Successful!'}, status=status.HTTP_200_OK)
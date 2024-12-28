import re
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
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

        errors = {'email': [], 'password': [], 'others': []}

        if User.objects.filter(email=email).exists():
            errors['email'].append('A user with this email already exists.')

        if password1=='' or password2=='':
            errors['password'].append('Password field cannot be empty.')

        if password1 != password2:
            errors['password'].append('Password Mismatch.')

        if len(errors['email'])>0 or len(errors['password'])>0:
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

        user_data = {
            'username': email,
            'email': email,
            'password': make_password(password1),
            'first_name': first_name,
            'last_name': last_name
        }
        user_form = UserRegistrationForm(user_data)

        if user_form.is_valid():
            print('form is valid')
        else:
            for error_tuple in user_form.errors.items():
                for error in error_tuple[1]:
                    if error_tuple[0]=='email':
                        errors['email'].append(error)
                    elif error_tuple[0]=='password':
                        errors['password'].append(error)

            if len(errors['email'])>0 or len(errors['password'])>0:
                return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e:
                errors['password'].append(error)
        
        if len(errors['email'])>0 or len(errors['password'])>0:
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create the User object from form validated data and save them to the database
            user = user_form.save()                                             
            UserProfile.objects.create(user=user, profile_type=profile_type)
        except Exception as e:
            errors['others'].append('User Account could not be created')

        if len(errors['others'])>0:
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Registration Successful!'}, status=status.HTTP_201_CREATED)
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import AccessToken
from owt_api.serializers import UserSerializer


# For register feature --> should be in 2 steps : 1. create user when he is registered 2. create initial data when
# user is created at his first connection and only if 'None'/null is assigned to last_login when registering he could
# specify his initial data

def register_user(data):
    data['password'] = make_password(data['password'])
    data['is_superuser'] = False
    data['is_staff'] = False
    data['is_active'] = True
    data['last_login'] = None
    data['username'] = data['username'].lower().strip()
    data['email'] = data['email'].lower().strip()

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()

        # Generate JWT
        token = AccessToken.for_user(user)
        # Create a response and set the Authorization header with the JWT
        response = HttpResponse(status=status.HTTP_201_CREATED)
        response['Authorization'] = f'Bearer {str(token)}'
        return response
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

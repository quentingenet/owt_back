from django.contrib.auth.hashers import make_password
from owt_api.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

# For register feature --> should be in 2 steps : 1. create user when he is registered 2. create initial data when
# user is created at his first connection and only if 'None' is assigned to last_login when registering he could
# specify his initial data
def register_user(data):
    
    data['password'] = make_password(data['password'])
    data['is_superuser'] = False
    data['is_staff'] = False
    data['is_active'] = True
    data['last_login'] = None
    data['username'] = data['username'].lower()
    data['email'] = data['email'].lower().trim()

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

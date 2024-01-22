from rest_framework import status
from rest_framework.response import Response
from owt_api.models import InitialData
from owt_api.serializers import InitialDataSerializer


def set_initial_data_first_connexion(data):
    serializer = InitialDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from owt_api.global_utils import check_first_connection
from .services import user_service, initial_data_service
from .models import Person, InitialData, WeightRecord, BodyMassIndex
from .serializers import PersonSerializer, InitialDataSerializer, WeightRecordSerializer, \
    BodyMassIndexSerializer, UserSerializer


from django.http import HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from owt_api.global_utils import check_first_connection
from .services import user_service, initial_data_service
from .models import Person, InitialData, WeightRecord, BodyMassIndex
from .serializers import PersonSerializer, InitialDataSerializer, WeightRecordSerializer, \
    BodyMassIndexSerializer, UserSerializer

class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()


class PersonModelViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Person.objects.all()


class InitialDataModelViewSet(ModelViewSet):
    serializer_class = InitialDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InitialData.objects.all()


class WeightRecordModelViewSet(ModelViewSet):
    serializer_class = WeightRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WeightRecord.objects.all()


class BodyMassIndexModelViewSet(ModelViewSet):
    serializer_class = BodyMassIndexSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BodyMassIndex.objects.all()


# New user registration
@api_view(['POST'])
def register_user_view(request):
    return user_service.register_user(request.data)


# After registration set initial data only if first connexion
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_initial_data_first_connexion_view(request):
    if request:
        user_id = request.user_id
        if check_first_connection(user_id):
            response = initial_data_service.set_initial_data_first_connexion(request.data)
            return response
        else:
            return HttpResponseForbidden("You are not allowed to access this resource")
    else:
        return HttpResponseForbidden("You are not allowed to access this resource")

# New user registration with call to service layer
@api_view(['POST'])
def register_user_view(request):
    return user_service.register_user(request.data)

# New user registration
@api_view(['POST'])
def register_user_view(request):
    return user_service.register_user(request.data)


# After registration set initial data only if first connexion
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_initial_data_first_connexion_view(request):
    if request:
        user_id = request.user_id
        if check_first_connection(user_id):
            response = initial_data_service.set_initial_data_first_connexion(request.data)
            return response
        else:
            return HttpResponseForbidden("You are not allowed to access this resource")
    else:
        return HttpResponseForbidden("You are not allowed to access this resource")


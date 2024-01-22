from django.contrib.auth.models import User
import jwt
from rest_framework.exceptions import AuthenticationFailed


def get_user_id_from_jwt(request):
    # Get the Authorization header
    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if auth_header is not None:
        # Split the header into 'Bearer' and the token
        auth_type, jwt_token = auth_header.split()

        if auth_type.lower() == 'bearer':
            try:
                # Decode the JWT token
                payload = jwt.decode(jwt_token, options={"verify_signature": False})

                # Get the user_id from the payload
                user_id = payload.get('user_id')

                return user_id
            except jwt.InvalidTokenError:
                raise AuthenticationFailed('Invalid token')
        else:
            raise AuthenticationFailed('Invalid Authorization header format. Expected "Bearer <token>"')
    else:
        raise AuthenticationFailed('Authorization header is missing')


def check_first_connection(user_id):
    user = User.objects.get(id=user_id)
    is_first_connection = user.last_login is None
    return is_first_connection


def check_user_id(user_id):
    return User.objects.get(id=user_id) is not None

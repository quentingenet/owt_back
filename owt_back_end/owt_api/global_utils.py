from django.contrib.auth.models import User


def check_first_connection(user_id):
    user = User.objects.get(id=user_id)
    is_first_connection = user.is_active is False
    return is_first_connection


def check_user_id(user_id):
    return User.objects.get(id=user_id) is not None

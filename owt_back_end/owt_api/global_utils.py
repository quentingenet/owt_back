from django.contrib.auth.models import User


def check_first_connection(user_id):
    return User.objects.get(id=user_id).last_login is None


def check_user_id(user_id):
    return User.objects.get(id=user_id) is not None

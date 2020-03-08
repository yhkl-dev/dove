from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_obj(user_id):
    try:
        return User.ordering.get(pk=user_id)
    except User.DoesNotExist:
        return None

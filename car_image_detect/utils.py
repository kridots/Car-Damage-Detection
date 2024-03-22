from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_superuser

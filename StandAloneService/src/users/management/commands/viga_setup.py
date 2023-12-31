import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured

EMAIL_HOST_PASSWORD = "1234"
# EMAIL_HOST_PASSWORD = os.environ.get('VIGA_HOST_PASSWORD')
if not EMAIL_HOST_PASSWORD:
    raise ImproperlyConfigured("'VIGA_HOST_PASSWORD' environment variable is unset")

User = get_user_model()

email_superuser = 'superuser@standaloneservice.com'

help_message = f"""
Sets up the DB, creating:
1) superuser with admin rights (Email: {email_superuser})
"""


class Command(BaseCommand):
    """
    viga_setup: Command to set-up database for the application
    """
    help = help_message

    def handle(self, *args, **kwargs):
        if not User.objects.filter(email=email_superuser).exists():
            User.objects.create_superuser(first_name="Super User",
                                          email=email_superuser,
                                          password=EMAIL_HOST_PASSWORD)
            print('Super-User Created!')
        print('Viga Set-Up Complete!')

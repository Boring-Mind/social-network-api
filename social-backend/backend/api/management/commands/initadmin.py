from decouple import config
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = config("DJANGO_SUPERUSER_USERNAME")
        email = config("DJANGO_SUPERUSER_EMAIL")
        password = config("DJANGO_SUPERUSER_PASSWORD")

        if not User.objects.filter(username=username).exists():
            print(f"Creating account for {username} ({email})")
            User.objects.create_superuser(
                email=email, username=username, password=password
            )
            print("Successfully created admin user")
        else:
            print("Admin account has already been initialized.")

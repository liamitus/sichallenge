import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        username = os.environ['ADMIN_USERNAME']
        email = os.environ['ADMIN_EMAIL']
        password = os.environ['ADMIN_PW']
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(username, email, password)

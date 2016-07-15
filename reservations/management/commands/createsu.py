import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        name = os.environ.get('ADMIN_NAME')
        email = os.environ.get('ADMIN_EMAIL')
        password = os.environ.get('ADMIN_PASSWORD')

        name = name if name else 'django_admin'
        email = email if email else 'admin@admin.com'
        password = password if password else 'please_dont_hack'
        
        if not User.objects.filter(username=name).exists():
            User.objects.create_superuser(name, email, password)

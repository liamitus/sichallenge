import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        email = os.environ.get('ADMIN_EMAIL') if not None else 'admin@admin.com'
        password = os.environ.get('ADMIN_PASSWORD') if not None else 'please_dont_hack'
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', email, password)

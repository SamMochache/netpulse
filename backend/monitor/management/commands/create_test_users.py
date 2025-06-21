# backend/monitor/management/commands/create_test_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class Command(BaseCommand):
    help = 'Create test users for development'

    def handle(self, *args, **options):
        # Create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created admin user: admin/admin123'))
        else:
            self.stdout.write(self.style.WARNING(f'Admin user already exists'))

        # Create analyst user
        analyst_user, created = User.objects.get_or_create(
            username='analyst',
            defaults={
                'email': 'analyst@example.com',
                'role': 'analyst'
            }
        )
        if created:
            analyst_user.set_password('analyst123')
            analyst_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created analyst user: analyst/analyst123'))
        else:
            self.stdout.write(self.style.WARNING(f'Analyst user already exists'))

        # Create tokens for both users
        admin_token, created = Token.objects.get_or_create(user=admin_user)
        analyst_token, created = Token.objects.get_or_create(user=analyst_user)

        self.stdout.write(self.style.SUCCESS(f'Admin token: {admin_token.key}'))
        self.stdout.write(self.style.SUCCESS(f'Analyst token: {analyst_token.key}'))
        self.stdout.write(self.style.SUCCESS('Test users created successfully!'))
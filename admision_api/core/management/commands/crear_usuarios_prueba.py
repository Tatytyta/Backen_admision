from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crea usuarios de prueba: un administrador y un usuario normal'

    def handle(self, *args, **kwargs):
        # Crear usuario administrador
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='Usuario',
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(self.style.SUCCESS(
                f'✅ Usuario administrador creado: admin / admin123'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                'Usuario "admin" ya existe'
            ))

        # Crear usuario normal
        if not User.objects.filter(username='user').exists():
            user = User.objects.create_user(
                username='user',
                email='user@example.com',
                password='user123',
                first_name='Usuario',
                last_name='Normal',
                is_staff=False,
                is_superuser=False
            )
            self.stdout.write(self.style.SUCCESS(
                f'✅ Usuario normal creado: user / user123'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                'Usuario "user" ya existe'
            ))

        self.stdout.write(self.style.SUCCESS(
            '\n📋 Resumen de usuarios:\n'
            '  - Administrador: admin / admin123 (acceso completo)\n'
            '  - Usuario normal: user / user123 (solo lectura)\n'
        ))

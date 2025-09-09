from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates a new superuser with predefined credentials'

    def handle(self, *args, **options):
        username = 'jtanabalon'
        email = 'jtanabalon@example.com'  # Puedes cambiar este email
        password = '196065792Tt#'  # Cambia esta contraseña por la que tú quieras
        
        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'El usuario "{username}" ya existe.')
            )
            # Actualizar la contraseña del usuario existente
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Contraseña actualizada para el usuario "{username}".')
            )
        else:
            # Crear nuevo superusuario
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Superusuario "{username}" creado exitosamente.')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Username: {username}')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Password: {password}')
        )

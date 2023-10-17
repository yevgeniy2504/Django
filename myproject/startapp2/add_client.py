from .models import Client
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Add new client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        name = options['name']
        email = options['email']
        phone = options['phone']
        address = options['address']
        try:
            Client.objects.create(name=name, email=email, phone=phone, address=address)
        except:
            raise CommandError('Client already exists')
        self.stdout.write(self.style.SUCCESS('Client "%s" successfully added' % name))

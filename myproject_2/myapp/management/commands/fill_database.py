from django.core.management.base import BaseCommand
from ...models import Client, Product, Order
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Заполняет базу данных случайными данными'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of fake data to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            client = Client.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date=fake.date_time_this_decade()
            )
            product = Product.objects.create(
                name=fake.word(),
                description=fake.text(),
                price=fake.random_number(digits=4),
                quantity=fake.random_int(min=1, max=100),
                date=fake.date_time_this_decade()
            )
            order = Order.objects.create(
                client=client,
                total=fake.random_number(digits=4),
                date=fake.date_time_this_decade()
            )
            order.product.add(product)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))

# #Создайте три модели Django: клиент, товар и заказ.
#
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров.
# Товар может входить в несколько заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
#
# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
#
# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
#
#     Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой ба
#

from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    # функция создания заказа

    @staticmethod
    def create_order(self, client, product, total):
        order = self.create(client=client, product=product, total=total)
        return order

    def __str__(self):
        return self.client.name

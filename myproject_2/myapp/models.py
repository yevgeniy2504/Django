# Создайте три модели Django: клиент, товар и заказ.
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

from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.client.name
    
# Задание 3
#
# Path: django/myproject_2/myapp/views.py
# Создайте представление, которое будет выводить список всех клиентов, зарегистрированных в системе.
#
# Path: django/myproject_2/myapp/urls.py
# Создайте URL-адрес для представления из предыдущего задания.
#
# Path: django/myproject_2/myapp/templates/myapp/clients.html
# Создайте шаблон, который будет выводить список всех клиентов, зарегистрированных в системе.
#
# Path: django/myproject_2/myapp/templates/myapp/base.html
# Создайте базовый шаблон, от которого будут наследоваться все остальные шаблоны.
#
# Path: django/myproject_2/myapp/templates/myapp/index.html
# Создайте шаблон, который будет выводить ссылку на список всех клиентов, зарегистрированных в системе.
#
# Path: django/myproject_2/myapp/urls.py
# Добавьте URL-адрес для представления из предыдущего задания.
#
# Path: django/myproject_2/myapp/views.py
# Добавьте представление, которое будет выводить список всех товаров, добавленных в систему.
#
# Path: django/myproject_2/myapp/templates/myapp/products.html
# Создайте шаблон, который будет выводить список всех товаров, добавленных в систему.
#
# Path: django/myproject_2/myapp/templates/myapp/index.html
# Добавьте ссылку на список всех товаров, добавленных в систему.
#
# Path: django/myproject_2/myapp/urls.py
# Добавьте URL-адрес для представления из предыдущего задания.
#
# Path: django/myproject_2/myapp/views.py
# Добавьте представление, которое будет выводить список всех заказов, оформленных в системе.
#
# Path: django/myproject_2/myapp/templates/myapp/orders.html
# Создайте шаблон, который будет выводить список всех заказов, оформленных в системе.
#
# Path: django/myproject_2/myapp/templates/myapp/index.html
# Добавьте ссылку на список всех заказов, оформленных в системе.
#
# Path: django/myproject_2/myapp/urls.py
# Добавьте URL-адрес для представления из предыдущего задания.
#
# Path: django/myproject_2/myapp/views.py
# Добавьте представление, которое будет выводить список всех товаров, добавленных в систему.
#
# Path: django/myproject_2/myapp/templates/myapp/products.html
# Создайте шаблон, который будет выводить список всех товаров, добавленных в систему.
#
# Path: django/myproject_2/myapp/templates/myapp/index.html
# Добавьте ссылку на список всех товаров, добавленных в систему.
#
# Path: django/myproject_2/myapp/urls.py
# Добавьте URL-адрес для представления из предыдущего задания.
#
# Path: django/myproject_2/myapp/views.py
# Добавьте представление, которое будет выводить список всех заказов, оформленных в системе.


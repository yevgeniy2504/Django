# Задание
#
# Продолжаем работать с товарами и заказами.
#
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
#
# Товары в списке не должны повторятся.

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Client, Product, Order
from django.views import View


class Hello(View):
    def get(self, request):
        return HttpResponse('Hello, World!')


class OrdersList(View):
    def get(self, request, year=None, month=None):
        if year is None and month is None:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
        elif year is not None and month is None:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=30))
        elif year is not None and month is not None:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=365))
        products = Product.objects.filter(order__in=orders).distinct()
        return render(request, 'orders_list.html', {'products': products})


class OrdersListMonth(View):

    def get(self, request, year=None, month=None):
        if year is None and month is None:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
        elif year is not None and month is None:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=30))
        elif year is not None and month is not None:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=365))
        products = Product.objects.filter(order__in=orders).distinct()
        return render(request, 'orders_list.html', {'products': products})



class OrdersListYear(View):
    def get(self, request, year=None):
        if year is None:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
        else:
            orders = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=365))
        products = Product.objects.filter(order__in=orders).distinct()
        return render(request, 'orders_list.html', {'products': products})










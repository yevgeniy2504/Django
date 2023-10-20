from django.urls import path
from .views import Hello, OrdersList, OrdersListMonth, OrdersListYear

urlpatterns = [
    path('', Hello.as_view()),
    path('orders_list/', OrdersList.as_view()),
    path('orders_list_month/', OrdersListMonth.as_view()),
    path('orders_list_year/', OrdersListYear.as_view()),
    path('orders_list_month/<int:year>/<int:month>/', OrdersListMonth.as_view()),
    path('orders_list_year/<int:year>/', OrdersListYear.as_view()),
]


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

# (venv) [yevgeniy@fedora myproject_2]$ python manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...
#
# Exception in thread django-main-thread:
# Traceback (most recent call last):
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/urls/resolvers.py", line 717, in url_patterns
#     iter(patterns)
# TypeError: 'module' object is not iterable
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "/usr/lib64/python3.11/threading.py", line 1045, in _bootstrap_inner
#     self.run()
#   File "/usr/lib64/python3.11/threading.py", line 982, in run
#     self._target(*self._args, **self._kwargs)
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/utils/autoreload.py", line 64, in wrapper
#     fn(*args, **kwargs)
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/core/management/commands/runserver.py", line 133, in inner_run
#     self.check(display_num_errors=True)
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/core/management/base.py", line 485, in check
#     all_issues = checks.run_checks(
#                  ^^^^^^^^^^^^^^^^^^
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/core/checks/registry.py", line 88, in run_checks
#     new_errors = check(app_configs=app_configs, databases=databases)
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/core/checks/urls.py", line 42, in check_url_namespaces_unique
#     all_namespaces = _load_all_namespaces(resolver)
#                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/core/checks/urls.py", line 72, in _load_all_namespaces
#     namespaces.extend(_load_all_namespaces(pattern, current))
#                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/core/checks/urls.py", line 61, in _load_all_namespaces
#     url_patterns = getattr(resolver, "url_patterns", [])
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/utils/functional.py", line 57, in __get__
#     res = instance.__dict__[self.name] = self.func(instance)
#                                          ^^^^^^^^^^^^^^^^^^^
#   File "/home/yevgeniy/Рабочий стол/git/venv/lib/python3.11/site-packages/django/urls/resolvers.py", line 725, in url_patterns
#     raise ImproperlyConfigured(msg.format(name=self.urlconf_name)) from e
# django.core.exceptions.ImproperlyConfigured: The included URLconf '<module 'myapp1' from '/home/yevgeniy/Рабочий стол/git/django/myproject_2/myapp1/__init__.py'>' does not appear to have any patterns in it. If you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import.
#

# Почему ошибка ?

# Потому что в файле django/myproject_2/myapp1/urls.py не указаны пути к представлениям. Добавим их:
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
#
# После этого запустим сервер и перейдем по адресу http://
#
#
#
#

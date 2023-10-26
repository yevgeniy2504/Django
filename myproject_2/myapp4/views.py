from django.shortcuts import render


def index(request):
    return render(request, 'myapp4/index.html')


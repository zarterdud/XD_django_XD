# from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("<body>Hello, word</body>")


def home(request):
    return HttpResponse('<body>Главная</body>')

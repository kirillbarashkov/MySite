from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):  # HttpRequest
    return HttpResponse('Главная страница приложения My Site.')


def projects(request, project_name):
    return HttpResponse(f"<h1>Список проектов</h1><p>{project_name}</p>")

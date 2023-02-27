from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить проект', 'url_name': 'add_project'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]


def main_page(request):
    posts = Main.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'Main/main_page.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'Main/about.html', context=context)


def addproject(request):
    return HttpResponse('Добавление проекта')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exseption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение проекта с id = {post_id}')


def show_category(request, cat_id):
    posts = Main.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id,
    }

    return render(request, 'Main/main_page.html', context=context)

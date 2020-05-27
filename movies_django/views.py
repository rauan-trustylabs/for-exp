from django.shortcuts import render
from django.http import HttpResponse

# данный модуль отвечает за то что видит клиент когда делает запрос на твой сайт
# ты можешь прописать что будет на странице. на пример на странице /movies ты должен выставить список фильмов
def index(request):
    return HttpResponse('Hello, welcome to the index page.')



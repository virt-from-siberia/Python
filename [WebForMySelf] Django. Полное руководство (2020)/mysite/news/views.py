from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.


def index(request):
    news = News.objects.all()
    context = {'news': news, 'title': 'Список новостей'}
    return render(request, 'news/index.html', context)

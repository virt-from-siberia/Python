from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


# Create your views here.


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {'news': news, 'categories': categories, 'title': 'Список новостей'}

    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'categories': categories, 'title': 'Список новостей', 'category': category}

    return render(request, template_name='news/category.html', context=context)

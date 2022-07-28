from django.shortcuts import render, get_list_or_404
from .models import News, Category


# Create your views here.


def index(request):
    news = News.objects.all()
    context = {'news': news, 'title': 'Список новостей'}

    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'title': 'Список новостей', 'category': category}

    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_list_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

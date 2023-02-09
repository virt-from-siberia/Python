from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'items': items, 'categories': categories
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            print('if')

            return redirect('/login/')

    else:
        form = SignupForm()

    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

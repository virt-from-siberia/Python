from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    the_password = 'testing'
    return render(request, 'generator/home.html', {password: the_password})


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDIFJIKHFYLKJFLKFDGJDLFKGJL'))
    if request.GET.get('special'):
        characters.extend(list('%$#*()&^%$3@(*)'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'about/about.html')

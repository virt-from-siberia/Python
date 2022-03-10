from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    the_password = 'testing'
    return render(request, 'generator/home.html', {password: the_password})


def password(request):
    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = 10

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})

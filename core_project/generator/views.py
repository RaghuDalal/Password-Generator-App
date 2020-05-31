from django.shortcuts import render
from django.http import HttpResponse

import random

def home(request):
    """Display the homepage"""
    return render(request, 'generator/home.html')

def about(request):
    """Display about section of the WebApp"""
    about = 'This is a pasword generator created by Raghvender. Enjoy fam!'

    return render(request, 'generator/about.html', {'display_about': about})

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
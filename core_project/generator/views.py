from django.shortcuts import render
from django.http import HttpResponse

import random

def home(request):
    """Display the homepage"""
    return render(request, 'generator/home.html')

def about(request):
    """Display about section of the WebApp"""
    about = 'This is a pasword generator created by Raghu Dalal. Enjoy fam!'

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

    message = 'Could not create password shorter than 6 characters!'

    if length <= 5:
        return render(request, 'generator/error.html', {'error_message': message})

    limit_message = 'Password is too long!'

    if length >= 23:
        return render(request, 'generator/large_pass_error.html', {'max_limit': limit_message})

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import random
import string

from .models import URL

def create_code():
    character_list = string.digits + string.ascii_letters + string.punctuation
    code_length = 5
    password = ''
    for i in range(0, code_length):
        code = code + random.choice(character_list)

def index(request):
    # Render HTML and the url form.
    return render(request, 'reducer/index.html', {})

def shorten(request):
    # Create an URL in the database with a generated code.
    # model = URL()
    # request.POST

    pass

def redirect(request, code):
    # Get a url from the database with the specified code and redirect the user.
    # eg. localhost:8000/reducer/9x82fc9
    model = get_object_or_404(URL, code=code)
    return redirect(model.url)
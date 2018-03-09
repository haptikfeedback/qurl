from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
import random
import string

from .models import URL

def create_code():
    character_list = string.digits + string.ascii_letters
    code = ''
    for i in range(0, 6):
        code = code + random.choice(character_list)
    return(code)

def index(request):
    # Render HTML and the url form.
    return render(request, 'reducer/index.html')

def shorten(request):
    # Create an URL in the database with a generated code.
    model = URL()
    model.url = request.POST['url']
    model.code = create_code()
    model.save()

    return JsonResponse({'code': model.code})

def redirect(request, code):
    # Get a url from the database with the specified code and redirect the user.
    # eg. localhost:8000/reducer/9x82fc9
    model = get_object_or_404(URL, code=code)
    model.save()
    return HttpResponseRedirect(model.url)

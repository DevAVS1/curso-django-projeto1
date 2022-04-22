from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_view(request):
    return HttpResponse(f"""<h1> Uma linda response movida "{str(randint(0,50))}" </h1>""")


def my_recipes(request):
    return render(request, 'home.html')  # Arquivo será buscado em 'templates'

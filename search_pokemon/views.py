from django.shortcuts import render
from .services import logic

def about(request):
    return render(request, 'service/about.html')


def info_pokemon(request, name):
    return render(request, 'service/info.html', logic.pokemon_info(name))

from django.shortcuts import render
from django.http import JsonResponse
from .services import logic


def about(request):
    return render(request, 'service/about.html')


def info_pokemon(request, name):
    p = logic.pokemon_info(name)
    pokemon = {
        "name": p.name,
        "id": p.id,
        "weight": p.weight,
        "height": p.height
    }
    return JsonResponse(pokemon)

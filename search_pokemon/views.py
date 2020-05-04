from django.shortcuts import render
from django.http import JsonResponse
from .services import logic


def about(request):
    return render(request, 'service/about.html')


def info_pokemon(request, name):
    pokemon = logic.get_pokemon(name)
    if pokemon:
        return JsonResponse(pokemon)
    else:
        return JsonResponse({"Respuesta": "Pokémon no encontrado"})

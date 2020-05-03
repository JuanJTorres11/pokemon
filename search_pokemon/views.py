from django.shortcuts import render


def about(request):
    return render(request, 'service/about.html')


def info_pokemon(request, name):
    return render(request, 'service/info.html', {'name': name})

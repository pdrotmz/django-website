from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'nome': 'Pedro Tomáz'
    })

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return render(request, 'sobre.html')
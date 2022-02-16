from django.shortcuts import render
from .models import Model



def index(request):
    
    return render(request, 'team/index.html')


def players(request):
    models = Model.objects.all()
    return render(request, 'team/players.html', {'name' : 'Нападаючий', "models": models})

def gallery(request):
    return render(request, 'team/gallery.html')

def contact(request):
    return render(request, 'team/contact.html')


def bloh(request):
    return render(request, 'team/bloh.html')
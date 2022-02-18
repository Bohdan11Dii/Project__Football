from django.shortcuts import render
from .models import Model
from .models import Contact
from django.http import HttpResponse


def index(request):
    
    return render(request, 'team/index.html')


def players(request):
    models = Model.objects.all()
    return render(request, 'team/players.html', {'name' : 'Нападаючий', "models": models})

def gallery(request):
    return render(request, 'team/gallery.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US</h1>") 
    return render(request, 'team/contact.html')


def bloh(request):
    return render(request, 'team/bloh.html')
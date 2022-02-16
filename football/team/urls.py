from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('players', views.players, name='players'),
    path('gallery', views.gallery),
    path('contact', views.contact),
    path('bloh', views.bloh)
]



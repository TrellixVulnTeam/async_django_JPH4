from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    aiohttp_pokedex,
    fetch_pokedex,
    pokemon_detail
)

urlpatterns = [
    path('',  TemplateView.as_view(template_name='pokedex/pokedex.html'), name='pokedex_home'),
    path('aio-pokedex/', aiohttp_pokedex, name='aiohttp_pokedex'),
    path('fetch-pokedex/', fetch_pokedex, name='fetch_pokedex'),
    path('pokemon/<int:id>/', pokemon_detail, name='pokemon_detail'),
]

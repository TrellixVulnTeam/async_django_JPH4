from django.shortcuts import render
import aiohttp
import asyncio
from .utils import get_data
# Create your views here.


# async def playground(request):
#     pokedex = []
#     async with aiohttp.ClientSession() as session:
#         for num in range(1, 101):
#             async with session.get(f'https://pokeapi.co/api/v2/pokemon/{num}/') as response:
#                 pokemon = await response.json()
#                 pokedex.append(pokemon['name'])
    
#     return render(request, 'home/playground.html', {'pokedex': pokedex})

async def playground(request):
    return render(request, 'home/playground.html', {'title': "playground"})
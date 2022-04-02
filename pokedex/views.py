from django.shortcuts import render
from home.utils import get_data
import aiohttp
import asyncio

async def aiohttp_pokedex(request):
    if request.method == 'POST':
        actions = []
        data = []
        async with aiohttp.ClientSession() as session:
            for num in range(1, 152):
                url = f'https://pokeapi.co/api/v2/pokemon/{num}/'
                actions.append(asyncio.ensure_future(get_data(session, url)))
                
            pokemon_response = await asyncio.gather(*actions)
            for pokemon in pokemon_response:
                data.append(pokemon)
        return render(request, 'pokedex/aiohttp_pokedex.html', {'pokedex': data, 'title': "Pokedex"})
    
    return render(request, 'pokedex/aiohttp_pokedex.html', {'title': "Pokedex"} )

def fetch_pokedex(request):
    return render(request, 'pokedex/fetch_pokedex.html', {'title': 'Pokedex'})

async def pokemon_detail(request, id):
    data = []
    async with aiohttp.ClientSession() as session:
        url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
        async with session.get(url) as response:
            pokemon = await response.json()
    return render(request, 'pokedex/pokemon_detail.html', {'pokemon': pokemon})
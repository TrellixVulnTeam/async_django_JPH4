const pokemonContainer = document.querySelector('.pokemon-container')
const searchBar = document.querySelector('.search')
const btn = document.querySelector('.fetch-btn')


const addData = pokemon => {
    const html =`
    <div class="${pokemon.name} card mx-2 my-2 col-sm-6 col-md-4 col-lg-2" style="width: 18rem;">
        <img src="${pokemon.sprites.front_default}" alt="${pokemon.name} sprite">
        <div class="card-body">
            <h5 class="card-title poke-name">${pokemon.name}</h5>
            <a class='text-centered' href="/pokedex/pokemon/${pokemon.id}">Click here</a>
        </div>
    </div>
    `
    pokemonContainer.innerHTML += html
}

// fetch

// const getPokemon = () => {
//     for(let i=0; i < 152; i++){
//         fetch(`https://pokeapi.co/api/v2/pokemon/${i}/`)
//         .then((response) => {
//             return response.json()
//         }).then(pokemon => {
//             addData(pokemon)
//         }).catch((err) => {
//             console.log('rejected', err)
//         })
//     }
    
// }

const getPokemon = async () => {
    for(let i=1; i < 152; i++){
    url = `https://pokeapi.co/api/v2/pokemon/${i}/`
    const res = await fetch(url);
    const pokemon = await res.json();
    addData(pokemon)
    btn.classList.add('filtered')
    } 
}

const filterPokemon = (term) => {
    let pokeDiv = document.querySelectorAll('.poke-name')
    // add 
    Array.from(pokeDiv)
   .filter((pokemon) => !pokemon.textContent.includes(term))
   .forEach((pokemon) => pokemon.parentElement.parentElement.classList.add('filtered'))

    // takeaway 
    Array.from(pokeDiv)
   .filter((pokemon) => pokemon.textContent.includes(term))
   .forEach((pokemon) => pokemon.parentElement.parentElement.classList.remove('filtered'))
}

searchBar.addEventListener('keyup', () => {
    const term = searchBar.value.trim().toLowerCase()
    filterPokemon(term)
})
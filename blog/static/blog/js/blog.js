const playgroundContainer = document.querySelector('.playground-container')
const btn = document.querySelector('.data-btn')

const addData = (post) => {
    const html = `
    <div class="card col-8 mb-5" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">${post.title}</h5>
    <h6 class="card-subtitle mb-2 text-muted">${post.excerpt}</h6>
    <p class="card-text">${post.content.split('\n').join('<br/>').slice(0, 250)}.........</p>
    <a href="detail/${post.id}" class="card-link">Card link</a>
  </div>
</div>
    `
    playgroundContainer.innerHTML += html
} 

const getPosts = async () => {
    url = 'http://127.0.0.1:8000/api/blog/'
    const res = await fetch(url);
    const posts = await res.json()
    posts.forEach(post => {
        addData(post)
    })
    btn.classList.add('filtered')
} 


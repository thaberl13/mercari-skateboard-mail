// const bart = document.getElementById('bart')
const bart = document.createElement('img')
bart.src="https://thumbs.gfycat.com/PreciousIdioticAlaskanhusky-max-1mb.gif"
bart.id="bart"
const test = document.getElementById('bart-append')
const thanks = document.createElement('h1')
thanks.innerText="Thanks for signing up!"

const submitButton = document.getElementById
('submit').addEventListener('click', ()=>{
    test.appendChild(bart)
    test.appendChild(thanks)
    alert('Thanks for subscribing!')
})
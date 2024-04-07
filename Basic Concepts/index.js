console.log('hello world')

const testEl = document.getElementById('test-el')

testEl.textContent = 'bye bye'

testEl.addEventListener('click', ()=> {
  console.log('click')
  testEl.innerHTML = "<b>clicked</b>"
}) 

testEl.addEventListener('mouseover', ()=>
{
  console.log('on')
})

testEl.addEventListener('mouseout', ()=>
{
  console.log('off')
})

document.addEventListener('scroll', ()=>
{
  const positionY = window.scrollY
  console.log(positionY)
})


// GET the data with ajax
const url = 'https://swapi.dev/api/people/'

$.ajax(
  {
    type: 'GET',
    url: url,
    sucess: function(response){
      console.log('jquery ajax', JSON.parse(req.responseText))
    },
    error: function(error)
    {
      console.log(error)
   }
  }
)


// 2. XMLHttpRequest
const req = new XMLHttpRequest()

req.addEventListener('readystatechange', ()=> {
  if (req.readyState==4){
    console,log('xhttp', req.responseText)
  }
})

req.open('GET', url)
req.send()


// 3. Fetch Method
console.log(fetch(url))
.then(resp=>resp.json()).then(data=>console.log('fetch', data))
.catach(err=> console.log(err))
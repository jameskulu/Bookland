var swiper = new Swiper('.swiper1', {
  // cssMode: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  // mousewheel: true,
  keyboard: true,

  effect: 'fade',
  speed: 1000,
  loop: true,

});

var swiper = new Swiper('.recently-viewed', {
  slidesPerView: 4,
  spaceBetween: 50,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    200: {
      slidesPerView: 1,
      spaceBetween: 20,
    },
    640: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 40,
    },
    1024: {
      slidesPerView: 4,
      spaceBetween: 50,
    },
  }
});

// -------- SLideshow Time Interval -------------



setInterval(function () { document.getElementsByClassName('swiper-button-next')[0].click(); }, 5000);





// ---------- Search toggle -------------

let search = document.getElementsByClassName('search-icon')[0]
let search_div = document.getElementsByClassName('home-search')[0]

search_div.style.opacity = '0'
search.onclick = () => {
  if (search_div.style.opacity === '0') {
    search_div.style.opacity = '1'
    search_div.style.pointerEvents = 'all'
    console.log('hello')
  }
  else if (search_div.style.opacity === '1') {
    search_div.style.opacity = '0';
    search_div.style.pointerEvents = 'none';
    search_div.style.zIndex = '99';
    console.log('hello')
  }
}
document.querySelector('.nav-bar-icon')
  .addEventListener('click', () => {
    search_div.style.opacity = '0';
    search_div.style.pointerEvents = 'none';
  });


// ---------------------------- Dark Mode -------------------------------


let checkbox = document.querySelector('input[name=theme]');
let checked = JSON.parse(localStorage.getItem('checkbox1zaal1'));

checkbox.addEventListener('change', function () {
  if (this.checked) {
    trans()
    document.documentElement.setAttribute('data-theme', 'dark')
    document.getElementById('logo-img').src = darkLogo
    localStorage.setItem("favorite", checkbox.value)
  } else {
    trans()
    localStorage.removeItem("favorite");
    document.documentElement.setAttribute('data-theme', 'light')
    document.getElementById('logo-img').src = lightLogo
  }
})
let trans = () => {
  document.documentElement.classList.add('transition');
  window.setTimeout(() => {
    document.documentElement.classList.remove('transition')
  }, 1000)
}

// ------------ Navigation toggle ----------------

document.querySelector('.nav-bar-icon')
  .addEventListener('click', () => document.querySelector('.nav').classList.toggle('show'));
document.querySelector('.nav-bar-icon')
  .addEventListener('click', () => document.querySelector('.login-signup-nav').classList.toggle('show2'));
document.querySelector('.nav-bar-icon')
  .addEventListener('click', () => document.querySelector('.search-cart').classList.toggle('show3'));



// ------ Message Close ----

let messageCloseBtn = document.querySelector('#message-close-btn')
let messageDiv = document.querySelector('#success');

messageCloseBtn.addEventListener("click", function () {
  messageDiv.style.display = "none";
})

setInterval(function () {
  messageDiv.style.display = 'none'
}, 7000)

const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {

    navbar.classList.add('scrolled');
  } else {

    navbar.classList.remove('scrolled');
  }
});

const navMobile = document.querySelector('.navbar__mobile');

function navClose() {
    navMobile.style.width = "0";
    setTimeout(() => {
        navMobile.style.display = "none";
        document.body.classList.remove('no-scroll');
    }, 500); 
}

function navOpen() {
    navMobile.style.display = "flex";
    document.body.classList.add('no-scroll');
    setTimeout(() => {
        navMobile.style.width = "100%";
    }, 10); 

}
const navbar = document.querySelector('.navbar');

// Add an event listener for scrolling
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    // Add the "scrolled" class if scrolled down
    navbar.classList.add('scrolled');
  } else {
    // Remove the "scrolled" class when at the top
    navbar.classList.remove('scrolled');
  }
});

const navMobile = document.querySelector('.navbar__mobile');

function navClose() {
    navMobile.style.width = "0";
    setTimeout(() => {
        navMobile.style.display = "none";
        // document.body.classList.remove('no-scroll');
    }, 500); // Match the transition duration
}

function navOpen() {
    navMobile.style.display = "flex";
    // document.body.classList.add('no-scroll');
    setTimeout(() => {
        navMobile.style.width = "100%";
    }, 10); // Small delay to trigger the transition
}

// Simulate hover effect on touch devices
const dropdowns = document.querySelectorAll('.navbar__dropdown');

dropdowns.forEach(dropdown => {
  dropdown.addEventListener('touchstart', () => {
    dropdown.classList.toggle('hover');
  });
});


let i = 0;
const txt = 'Let\'s Talk About Your Mental Health';
const speed = 70;

function typeWriter() {
  if (i < txt.length) {
    document.querySelector('.flex__headtitle').innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

addEventListener('load', typeWriter);
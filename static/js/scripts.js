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
    }, 500); // Match the transition duration
}

function navOpen() {
    navMobile.style.display = "flex";
    setTimeout(() => {
        navMobile.style.width = "100%";
    }, 10); // Small delay to trigger the transition
}
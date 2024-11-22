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
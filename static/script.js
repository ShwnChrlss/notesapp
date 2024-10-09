// script.js
// Add event listeners for logout buttons
document.addEventListener("DOMContentLoaded", function () {
  const logoutLinks = document.querySelectorAll('a[href*="logout"]');
  logoutLinks.forEach(link => {
      link.addEventListener('click', function (event) {
          if (!confirm("Are you sure you want to log out?")) {
              event.preventDefault(); // Prevent the default action if the user cancels
          }
      });
  });
});

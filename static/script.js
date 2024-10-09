// script.js

// Function to open the sidebar
function openNav() {
  document.getElementById("sidebar").style.left = "0";
}

// Function to close the sidebar
function closeNav() {
  document.getElementById("sidebar").style.left = "-250px";
}

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

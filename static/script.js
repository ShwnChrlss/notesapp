// script.js

// Add JavaScript functions for sidebar navigation
// Function to open the sidebar
function openNav() {
  document.getElementById("sidebar").style.left = "0"; // Show sidebar
}

// Function to close the sidebar
function closeNav() {
  document.getElementById("sidebar").style.left = "-250px"; // Hide sidebar
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

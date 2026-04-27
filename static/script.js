// JavaScript code to show the login overlay
document.getElementById('loginLink').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default link behavior
    document.getElementById('overlay').style.display = 'flex'; // Show the overlay
});

document.getElementById('exploreBtn').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'flex'; // Show the overlay
});

document.getElementById('cancelBtn').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'none'; // Hide the overlay
});



// loading js
document.addEventListener("DOMContentLoaded", function() {
    // Create the text 'Dyslexia' and append each letter to the loading screen
    const loadingText = document.getElementById('loadingText');
    const word = 'Dyslexia';
    
    word.split('').forEach((letter, index) => {
        const span = document.createElement('span');
        span.textContent = letter;
        loadingText.appendChild(span);
    });

    // Hide the loading screen once the page is fully loaded
    window.addEventListener('load', function() {
        const loadingScreen = document.getElementById('loadingScreen');
        const pageContent = document.getElementById('pageContent');

        // Remove loading screen and display page content
        loadingScreen.style.display = 'none';
        pageContent.style.display = 'block';
    });
});


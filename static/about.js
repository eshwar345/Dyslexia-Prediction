

// Function to toggle content visibility
function toggleContent(button) {
    const content = button.closest('.c1').querySelector('.content');
    content.style.display = content.style.display === 'block' ? 'none' : 'block';
}


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




            
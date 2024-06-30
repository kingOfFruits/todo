function validateForm() {
    var title = document.getElementById('title').value;
    if (title === '') {
        document.getElementById('alertMessage').textContent = "Title cannot be empty.";
        return false; // Prevent form submission
    } else {
        document.getElementById('alertMessage').textContent = ""; // Clear any previous messages
        return true; // Allow form submission
    }
}
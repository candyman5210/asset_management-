// script.js
function validateLoginForm() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Please enter both email and password.");
        return false;
    }

    // Further validation can be added here

    return true;
}

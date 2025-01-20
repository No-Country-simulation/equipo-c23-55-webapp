// Limpia el formulario de login
const loginForm = document.getElementById('login-form');
if (loginForm) {
    loginForm.addEventListener('submit', function(event) {
        event.target.reset(); // Limpia los campos después del envío
    });
}

// Limpia el formulario de registro
const registroForm = document.getElementById('registro-form');
if (registroForm) {
    registroForm.addEventListener('submit', function(event) {
        event.target.reset(); // Limpia los campos después del envío
    });
}

function validarContraseñas() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm-password').value;

    if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden.");
        return false;
    }
    return true;
}

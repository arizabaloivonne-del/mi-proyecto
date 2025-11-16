console.log("Michelle Jewelry JS cargado correctamente");

document.addEventListener('DOMContentLoaded', function () {
    // Ocultar textos de ayuda
    const helpTexts = document.querySelectorAll('form small, form ul.helptext, form li.helptext');
    helpTexts.forEach(function (el) {
        el.style.display = 'none';
    });

    // Validación personalizada al enviar el formulario
    const form = document.querySelector('form');
    form.addEventListener('submit', function (e) {
        const email = document.getElementById('id_email');
        const pass1 = document.getElementById('id_password1');
        const pass2 = document.getElementById('id_password2');

        // Validar correo electrónico
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email && !emailRegex.test(email.value)) {
            alert('Por favor ingresa un correo electrónico válido.');
            e.preventDefault();
            return;
        }

        // Validar que las contraseñas coincidan
        if (pass1 && pass2 && pass1.value !== pass2.value) {
            alert('Las contraseñas no coinciden.');
            e.preventDefault();
            return;
        }

        // Validar longitud mínima de contraseña
        if (pass1 && pass1.value.length < 8) {
            alert('La contraseña debe tener al menos 8 caracteres.');
            e.preventDefault();
            return;
        }
    });
});

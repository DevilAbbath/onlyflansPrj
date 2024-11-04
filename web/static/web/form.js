console.log("Script Loaded....");
document.getElementById("contactForm").onsubmit = function(event) {
    event.preventDefault(); // Evita el envío estándar del formulario
    const formData = new FormData(this);

    fetch(this.action, {
        method: "POST",
        body: formData,
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Mostrar el modal de éxito
            var successModal = new bootstrap.Modal(document.getElementById('successModal'));
            successModal.show();
            // Limpiar el formulario
            document.getElementById("contactForm").reset();
        } else {
            // Manejar errores de validación
            console.log("Errores:", data.errors);
            // Puedes mostrar los errores en el formulario aquí si lo deseas
        }
    })
    .catch(error => console.error("Error:", error));
};

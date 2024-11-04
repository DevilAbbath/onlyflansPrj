document.addEventListener("DOMContentLoaded", function() {
    const navbar = document.getElementById("mainNav");

    if (!document.body.classList.contains("solid-navbar")) {
        window.addEventListener("scroll", function() {
            if (window.scrollY > 100) {
                navbar.classList.add("navbar-shrink");
            } else {
                navbar.classList.remove("navbar-shrink");
            }
        });
    } else {
        // Asegura que la clase navbar-shrink esté siempre presente en páginas no principales
        navbar.classList.add("navbar-shrink");
    }
});

document.addEventListener("DOMContentLoaded", () => {

    const Contenido = document.getElementById("contenido");

    function cargarPagina(url) {
        fetch(url, {
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(res => res.text())
        .then(html => {
            Contenido.innerHTML = html;
            history.pushState(null, "", url);
        });
    }

    document.querySelectorAll(".panel-link").forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            cargarPagina(this.href);
        });
    });

    let path = window.location.pathname;

    if (path === "/dashboard/admin") {
        path = "/dashboard/admin/inicio";
        path = "/dashboard/admin/casos";
        path = "/dashboard/admin/entidades";
        path = "/dashboard/admin/usuarios";
    }

    cargarPagina(path);

});
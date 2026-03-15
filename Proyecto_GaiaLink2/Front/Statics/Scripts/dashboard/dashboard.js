document.addEventListener("DOMContentLoaded", () => {
    const token = localStorage.getItem("Auth_Token") || sessionStorage.getItem("Auth_Token");
    if (!token) {
        window.location.href = "/login";
    }

    if(document.getElementById("Button_Cerrar")){
        document.getElementById("Button_Cerrar").addEventListener("click", () => {
            localStorage.removeItem("Auth_Token")
            sessionStorage.removeItem("Auth_Token")
            window.location.href = "/login";
        })
    }

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

    if (path === "/dashboard") {
        path = "/dashboard/inicio";
    }

    cargarPagina(path);

});
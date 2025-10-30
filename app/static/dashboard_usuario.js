document.addEventListener("DOMContentLoaded", () => {
    const cuadros = document.querySelectorAll('.Selector1, .Cuadro1[data-target], .Boton[data-target]');
    const frames = document.querySelectorAll('.Frame, .Frame1');
    const form = document.querySelector(".Buscar_Entidad_Contenedor2");
    const submitButton = form ? form.querySelector(".Formulario_CrearCaso_Boton2") : null;
    const fields = form ? form.querySelectorAll("input, select") : [];

    cuadros.forEach(cuadro => {
        cuadro.addEventListener('click', () => {
            const target = cuadro.getAttribute('data-target');
            if (target) {
                if (window.location.pathname.includes("/casos") && target !== "FrameVerCasos") {
                    window.location.href = "/dashboard/user?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/entidad/buscar") && target !== "FrameBuscarEntidad2") {
                    window.location.href = "/dashboard/user?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/persona/datos") && target !== "FrameVerDatos") {
                    window.location.href = "/dashboard/user?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/persona/modificar/enviar") && target !== "FrameModificarDatos") {
                    window.location.href = "/dashboard/user?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/persona/modificar") && target !== "FrameModificarDatos") {
                    window.location.href = "/dashboard/user?frame=" + target;
                    return;
                }

                frames.forEach(frame => frame.classList.remove('visible'));
                document.getElementById(target)?.classList.add('visible');
            }
        });
    });

    document.querySelectorAll(".Boton_VerPassword").forEach((boton) => {
        const input = boton.nextElementSibling;
        const icono = boton.querySelector("img");

        boton.addEventListener("click", () => {
            if (input.type === "password") {
                input.type = "text";
                icono.src = "/static/img/Ver.svg";
            } else {
                input.type = "password";
                icono.src = "/static/img/NoVer.svg";
            }
        });
    });

    document.getElementById("formEliminarUsuario")?.addEventListener("submit", function(e) {
        e.preventDefault();

        if (confirm("¿Estás seguro de eliminar tu cuenta? Esta acción no se puede deshacer.")) {
            this.submit();
        }
    });

    window.abrirModal = function(id) {
        document.getElementById(id).style.display = "block";
    }

    window.cerrarModal = function(id) {
        document.getElementById(id).style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target.classList.contains("modal")) {
            event.target.style.display = "none";
        }
    }

    if (form && submitButton) {
        const originalValues = {};
        fields.forEach(field => {
            originalValues[field.name] = field.value;
        });

        submitButton.disabled = true;
        submitButton.style.opacity = "0.6";
        submitButton.style.cursor = "not-allowed";

        function verificarCambios() {
            let cambioDetectado = false;

            fields.forEach(field => {
                if (field.value !== originalValues[field.name]) {
                    cambioDetectado = true;
                }
            });

            if (cambioDetectado) {
                submitButton.disabled = false;
                submitButton.style.opacity = "1";
                submitButton.style.cursor = "pointer";
            } else {
                submitButton.disabled = true;
                submitButton.style.opacity = "0.6";
                submitButton.style.cursor = "not-allowed";
            }
        }

        fields.forEach(field => {
            field.addEventListener("input", verificarCambios);
            field.addEventListener("change", verificarCambios);
        });
    }
});

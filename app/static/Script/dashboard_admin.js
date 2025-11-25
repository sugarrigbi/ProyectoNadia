document.addEventListener("DOMContentLoaded", () => {
    const cuadros = document.querySelectorAll('.Selector1, .Cuadro1[data-target], .Boton[data-target]');
    const frames = document.querySelectorAll('.Frame, .Frame1');
    const campos = Array.from(document.querySelectorAll(".campo-modificar"));
    const btnModificar = document.getElementById("btnModificar");

    const campos2 = Array.from(document.querySelectorAll(".campo-modificar2"));
    const btnModificar2 = document.getElementById("btnModificar2");

    const ValoresOriginales2 = {};
    campos2.forEach(e => {
        ValoresOriginales2[e.name] = e.value;
    });
    function HayCambios2() {
        for (const campo2 of campos2){
            const original2 = ValoresOriginales2[campo2.name] ?? "";
            const actual2 = campo2.value;
            if (original2 !== actual2) return true;
        }
        return false;
    };
    function ValidarYActualizarBoton2() {
        btnModificar2.disabled = !HayCambios2();
    };
    campos2.forEach(e => {
        e.addEventListener("input", ValidarYActualizarBoton2)
        e.addEventListener("change", ValidarYActualizarBoton2);
    });


    const valoresOriginales = {};
    campos.forEach(c => {
        valoresOriginales[c.name] = c.value;
    });

    function hayCambios() {
        for (const campo of campos) {
            const original = valoresOriginales[campo.name] ?? "";
            const actual = campo.value;
            if (original !== actual) return true;
        }
        return false;
    }
    function validarYActualizarBoton() {
        btnModificar.disabled = !hayCambios();
    }    

    campos.forEach(c => {
        c.addEventListener("input", validarYActualizarBoton);
        c.addEventListener("change", validarYActualizarBoton);
    });

    cuadros.forEach(cuadro => {
        cuadro.addEventListener('click', () => {
            const target = cuadro.getAttribute('data-target');
            if (target) {
                if (window.location.pathname.includes("/dashboard/admin/casos/buscar") && target !== "FrameBuscarCasos") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/dashboard/admin/casos/crear") && target !== "FrameCrearCaso") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }  
                if (window.location.pathname.includes("/dashboard/admin/casos/modificar") && target !== "FrameModificarCasoBuscar") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }    
                
                if (window.location.pathname.includes("/dashboard/admin/entidades/buscar") && target !== "FrameBuscarEntidades") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/dashboard/admin/entidades/crear") && target !== "FrameCrearEntidades") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }  
                if (window.location.pathname.includes("/dashboard/admin/entidades/modificar") && target !== "FrameModificarEntidadesBuscar") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }                  



                if (window.location.pathname.includes("/entidad/buscar") && target !== "FrameBuscarEntidad2") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/persona/datos") && target !== "FrameVerDatos") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/persona/modificar/enviar") && target !== "FrameModificarDatos") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/persona/modificar") && target !== "FrameModificarDatos") {
                    window.location.href = "/dashboard/admin?frame=" + target;
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
        document.getElementById(id).style.display = "flex";
    }

    window.cerrarModal = function(id) {
        document.getElementById(id).style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target.classList.contains("modal")) {
            event.target.style.display = "none";
        }
    }

    window.filtrarCasos = function() {
        let input = document.getElementById("buscador").value.toLowerCase();
        let casos = document.querySelectorAll(".FrameVerCasos_Caso h3");

        casos.forEach((caso) => {
            let texto = caso.textContent.toLowerCase();
            if (texto.includes(input)) {
                caso.parentElement.style.display = "block";
            } else {
                caso.parentElement.style.display = "none";
            }
        });
    }    
    window.filtrarEntidades = function() {
        let input = document.getElementById("buscador2").value.toLowerCase();
        let entidades = document.querySelectorAll(".FrameVerCasos_Caso h3");

        entidades.forEach((entidad) => {
            let texto = entidad.textContent.toLowerCase();
            if (texto.includes(input)) {
                entidad.parentElement.style.display = "block";
            } else {
                entidad.parentElement.style.display = "none";
            }
        });
    } 

    validarYActualizarBoton();
    ValidarYActualizarBoton2();
});

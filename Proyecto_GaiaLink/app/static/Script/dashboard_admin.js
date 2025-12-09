document.addEventListener("DOMContentLoaded", () => {
    const cuadros = document.querySelectorAll('.Selector1, .Cuadro1[data-target], .Boton[data-target]');
    const frames = document.querySelectorAll('.Frame, .Frame1');
    const campos = Array.from(document.querySelectorAll(".campo-modificar"));
    const campos2 = Array.from(document.querySelectorAll(".campo-modificar2"));
    const campos3 = Array.from(document.querySelectorAll(".campo-modificar3"));
    const oscuro = document.getElementById("btnModoOscuro");
    const idioma = document.getElementById("btnIdiomaUnico");
    const modoGuardado = localStorage.getItem("modoOscuro");
    const idiomaGuardado = localStorage.getItem("idioma");
    const btnModificar = document.getElementById("btnModificar");
    const btnModificar2 = document.getElementById("btnModificar2");
    const btnModificar3 = document.getElementById("btnModificar3");    
    const ValoresOriginales = {};
    const ValoresOriginales2 = {};
    const ValoresOriginales3 = {};
    campos.forEach(c => {
        ValoresOriginales[c.name] = c.value;
    });
    campos.forEach(c => {
        c.addEventListener("input", ValidarYActualizarBoton);
        c.addEventListener("change", ValidarYActualizarBoton);
    });   
    campos2.forEach(e => {
        ValoresOriginales2[e.name] = e.value;
    });
    campos2.forEach(e => {
        e.addEventListener("input", ValidarYActualizarBoton2)
        e.addEventListener("change", ValidarYActualizarBoton2);
    }); 
    campos3.forEach(c => {
        ValoresOriginales3[c.name] = c.value;
    });
    campos3.forEach(c => {
        c.addEventListener("input", ValidarYActualizarBoton3);
        c.addEventListener("change", ValidarYActualizarBoton3);
    });       
    function HayCambios() {
        for (const campo of campos) {
            const original = ValoresOriginales[campo.name] ?? "";
            const actual = campo.value;
            if (original !== actual) return true;
        }
        return false;
    }    
    function HayCambios2() {
        for (const campo2 of campos2){
            const original2 = ValoresOriginales2[campo2.name] ?? "";
            const actual2 = campo2.value;
            if (original2 !== actual2) return true;
        }
        return false;
    };
    function HayCambios3() {
        for (const campo3 of campos3) {
            const original3 = ValoresOriginales3[campo3.name] ?? "";
            const actual3 = campo3.value;
            if (original3 !== actual3) return true;
        }
        return false;
    } 
    function ValidarYActualizarBoton() {
        if (btnModificar) btnModificar.disabled = !HayCambios();
    };
    function ValidarYActualizarBoton2() {
        if (btnModificar2) btnModificar2.disabled = !HayCambios2();
    };  
    function ValidarYActualizarBoton3() {
        if (btnModificar3) btnModificar3.disabled = !HayCambios3();
    };  
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
                if (window.location.pathname.includes("/dashboard/admin/casos/eliminar") && target !== "FrameEliminarCaso") {
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
                if (window.location.pathname.includes("/dashboard/admin/entidades/eliminar") && target !== "FrameEliminarEntidad") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }       
                if (window.location.pathname.includes("/dashboard/admin/usuarios/buscar") && target !== "FrameBuscarPersona") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }        
                if (window.location.pathname.includes("/dashboard/admin/usuarios/crear") && target !== "FrameCrearPersona") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }                            
                if (window.location.pathname.includes("/dashboard/admin/usuarios/modificar") && target !== "FrameModificarPersonaBuscar") {
                    window.location.href = "/dashboard/admin?frame=" + target;
                    return;
                }
                if (window.location.pathname.includes("/dashboard/admin/usuarios/eliminar") && target !== "FrameEliminarPersona") {
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
        let casos = document.querySelectorAll(".FrameVerCasos_Caso h4");

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
        let entidades = document.querySelectorAll(".FrameVerCasos_Caso h4");

        entidades.forEach((entidad) => {
            let texto = entidad.textContent.toLowerCase();
            if (texto.includes(input)) {
                entidad.parentElement.style.display = "block";
            } else {
                entidad.parentElement.style.display = "none";
            }
        });
    } 
    window.filtrarPersonas = function() {
        let input = document.getElementById("buscador3").value.toLowerCase();
        let personas = document.querySelectorAll(".FrameVerCasos_Caso");

        personas.forEach((persona, i) => {
            const h3 = persona.querySelector("h3");
            const h4 = persona.querySelector("h4");
            if (!h3 || !h4) {
                return;
            }

            const id = h3.textContent.toLowerCase().trim();;
            const nombre = h4.textContent.toLowerCase().trim();;
            const match = (id.includes(input) || nombre.includes(input));
            persona.style.display = match ? "" : "none";
        });
    }
    function ActualizarTextoTema() {
        const idioma = localStorage.getItem("idioma");
        const oscuroActivo = document.body.classList.contains("dark-mode");
        let texto = "";
        if (idioma === "es") texto = oscuroActivo ? "Oscuro" : "Claro";
        if (idioma === "en") texto = oscuroActivo ? "Dark" : "Light";
        if (idioma === "fr") texto = oscuroActivo ? "Sombre" : "Clair";
        document.getElementById("SunMoon2").textContent = texto;
    }
    idioma.addEventListener("click", () => {
        let idiomaActual = localStorage.getItem("idioma");
        if (idiomaActual === "es") idiomaActual = "en";
        else if (idiomaActual === "en") idiomaActual = "fr";
        else idiomaActual = "es";
        localStorage.setItem("idioma", idiomaActual);
        ActualizarTextoTema();
    });
    oscuro.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
        const idiomaGuardado = localStorage.getItem("idioma");
        const modoOscuroActivo = document.body.classList.contains("dark-mode");
        localStorage.setItem("modoOscuro", modoOscuroActivo ? "oscuro" : "claro");
        document.getElementById("SunMoon").src =
            modoOscuroActivo ? "/static/img/Moon.svg" : "/static/img/Sun.svg";
        if (idiomaGuardado === "es") {
            document.getElementById("SunMoon2").textContent = modoOscuroActivo ? "Oscuro" : "Claro";
        } else if (idiomaGuardado === "en") {
            document.getElementById("SunMoon2").textContent = modoOscuroActivo ? "Dark" : "Light";
        } else if (idiomaGuardado === "fr") {
            document.getElementById("SunMoon2").textContent = modoOscuroActivo ? "Sombre" : "Clair";
        }
    });
    if (modoGuardado === "oscuro") {
        document.body.classList.add("dark-mode");
        document.getElementById("SunMoon").src = "/static/img/Moon.svg";
        if (idiomaGuardado === "es") {
            document.getElementById("SunMoon2").textContent = "Oscuro";
        } else if (idiomaGuardado === "en") {
            document.getElementById("SunMoon2").textContent = "Dark";
        } else if (idiomaGuardado === "fr") {
            document.getElementById("SunMoon2").textContent = "Sombre";
        }
    } else if (modoGuardado === "claro") {
        document.getElementById("SunMoon").src = "/static/img/Sun.svg";
        if (idiomaGuardado === "es") {
            document.getElementById("SunMoon2").textContent = "Claro";
        } else if (idiomaGuardado === "en") {
            document.getElementById("SunMoon2").textContent = "Light";
        } else if (idiomaGuardado === "fr") {
            document.getElementById("SunMoon2").textContent = "Clair";
        }
    }
    ValidarYActualizarBoton();
    ValidarYActualizarBoton2();
    ValidarYActualizarBoton3();
});

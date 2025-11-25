document.addEventListener("DOMContentLoaded", () => {
    const frames = document.querySelectorAll(".Frame");
    const botones = document.querySelectorAll(".Boton_Sello");
    const solapa = document.querySelector(".solapa");
    const sello = document.querySelectorAll(".DebeOcultar");
    const sobre = document.getElementById("Sobre");
    const papel = document.getElementById("Papel");
    const simbolo = document.getElementById("Simbolo");
    const simbolo2 = document.getElementById("Simbolo2");
    const contador = document.querySelector(".contador");

    botones.forEach(boton => {
        boton.addEventListener("click", () => {
            const target = boton.getAttribute("data-target");
            solapa.classList.add("animar");

            sobre.src = "img/sobre-abierto.png"

            sello.forEach(sell => {
                sell.classList.add("ocultar");
            });

            simbolo.style.opacity = "0";
            simbolo2.style.opacity = "0";

            solapa.addEventListener("animationend", () => {
                setTimeout(() => {
                    if (target) {
                        frames.forEach(frame => frame.classList.remove("visible"));
                        document.getElementById(target)?.classList.add("visible");
                    }
                }, 400);
            }, { once: true });

        });
    });

    function actualizarContador() {
        const ahora = new Date();
        const anioActual = 2026;
        const fechaObjetivo = new Date(`${anioActual}-02-14T00:00:00`);

        const diferencia = fechaObjetivo - ahora;
        const format = n => String(n).padStart(2, '0');
        const dias = format(Math.floor(diferencia / 86400000));
        const horas = format(Math.floor((diferencia % 86400000) / 3600000));
        const minutos = format(Math.floor((diferencia % 3600000) / 60000));
        const segundos = format(Math.floor((diferencia % 60000) / 1000));
        
        document.getElementById("dias").textContent = `${dias}`;
        document.getElementById("horas").textContent = `${horas}`;
        document.getElementById("minutos").textContent = `${minutos}`;
        document.getElementById("segundos").textContent = `${segundos}`;

        if (diferencia < 0) {
            document.getElementById("dias").textContent = "¡Es hoy, es hoy!";
            document.getElementById("dias").style.fontFamily = "Dancing Script";

            document.getElementById("horas").classList.add("ocultar2");
            document.getElementById("minutos").classList.add("ocultar2");
            document.getElementById("segundos").classList.add("ocultar2");

            document.getElementById("faltan").textContent = "Felicidades!";
            document.getElementById("faltan").style.fontSize = "40px";
            document.getElementById("dias2").classList.add("ocultar2");
            document.getElementById("horas2").classList.add("ocultar2");
            document.getElementById("minutos2").classList.add("ocultar2");
            document.getElementById("segundos2").classList.add("ocultar2");

            const puntos = document.querySelectorAll(".puntos");
            puntos.forEach(punto => {
                punto.classList.add("ocultar2");
            });            
            contador.style.justifyContent = "center";
            clearInterval(intervalo);
        }
    }

    const frame1 = document.getElementById("Frame2");
    if (frame1) {
        frame1.classList.add("visible");
    }
    const intervalo = setInterval(actualizarContador, 1000);
    actualizarContador();
    
});
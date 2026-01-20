
const input = document.getElementById("Input_Contraseña");
const boton = document.getElementById("verPassword");
const icono = document.getElementById('iconoOjo');
const form = document.querySelector('.FormularioRegistrarse');
const Input_Contraseña = document.getElementById('Input_Contraseña');
const Input_Confirmar = document.getElementById('Input_Contraseña2');
function Enviar_Login() {
    window.open("login.html", "_self");
}
function Enviar_Calificanos() {
    window.open("calificanos.html", "_self");
}
function Enviar_Registro() {
    window.open("registrarse.html", "_self");
}
function Enviar_Home() {
    window.open("home.html", "_self");
}
function Enviar_Ayuda() {
    window.open("ayuda.html", "_self");
}
boton.addEventListener("click", () => {
    if (input.type === "password") {
        input.type = "text";
        icono.src = 'img/Ver.svg';
    } else {
        input.type = "password";
        icono.src = 'img/NoVer.svg';
    }
});

//asdasdasdasda
document.addEventListener("DOMContentLoaded", () => {
    const cuadros = document.querySelectorAll('.Selector');
    const frames = document.querySelectorAll('.Frame');

    cuadros.forEach(cuadro => {
        cuadro.addEventListener('click', () => {
            cuadros.forEach(c => c.classList.remove('activo'));
            cuadro.classList.add('activo');

            frames.forEach(frame => frame.classList.remove('visible'));
            const target = cuadro.getAttribute('data-target');
            const frameObjetivo = document.getElementById(target);
            if (frameObjetivo) {
                frameObjetivo.classList.add('visible');
            }
        });
    });
});
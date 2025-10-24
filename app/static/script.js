
const input = document.getElementById("Input_Contraseña");
const boton = document.getElementById("verPassword");
const icono = document.getElementById('iconoOjo');
const form = document.querySelector('.FormularioRegistrarse');
const Input_Contraseña = document.getElementById('Input_Contraseña');
const Input_Confirmar = document.getElementById('Input_Contraseña2');
function Enviar_Login() {
    window.location.href = "/login";
}
function Enviar_Calificanos() {
    window.location.href = "/calificanos";
}
function Enviar_Registro() {
    window.location.href = "/registro";
}
function Enviar_Home() {
    window.location.href = "/index";
}
function Enviar_Ayuda() {
    window.location.href = "/ayuda";
}
boton.addEventListener("click", () => {
    if (input.type === "password") {
        input.type = "text";
        icono.src = "static/img/Ver.svg"
    } else {
        input.type = "password";
        icono.src = "static/img/NoVer.svg";
    }
});
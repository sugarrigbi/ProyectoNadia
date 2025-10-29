
const input = document.getElementById("Input_Contraseña");
const input1 = document.getElementById("Input_Contraseña1");
const input2 = document.getElementById("Input_Contraseña2");
const boton = document.getElementById("verPassword");
const boton1 = document.getElementById("verPassword1");
const boton2 = document.getElementById("verPassword2");
const icono = document.getElementById('iconoOjo');
const icono1 = document.getElementById('iconoOjo1');
const icono2 = document.getElementById('iconoOjo2');
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
    window.location.href = "/";
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
boton1.addEventListener("click", () => {
    if (input1.type === "password") {
        input1.type = "text";
        icono1.src = "static/img/Ver.svg"
    } else {
        input1.type = "password";
        icono1.src = "static/img/NoVer.svg";
    }
});
boton2.addEventListener("click", () => {
    if (input2.type === "password") {
        input2.type = "text";
        icono2.src = "static/img/Ver.svg"
    } else {
        input2.type = "password";
        icono2.src = "static/img/NoVer.svg";
    }
});
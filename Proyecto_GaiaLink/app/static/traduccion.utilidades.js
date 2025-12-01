function actualizarImagenIdioma(idioma) {
    const logo = document.getElementById("logoIdioma");

    if (idioma === "es") {
        logo.src = "static/img/Español.svg";
    } else if (idioma === "en") {
        logo.src = "static/img/Ingles.svg";
    } else if (idioma === "fr") {
        logo.src = "static/img/Frances.svg";
    }
}
function CambiarIdioma(idioma){
    const traducciones = {
        es: { BotonIdioma: "Español" ,Inicio: "Inicio", Nosotros: "Nosotros", Contacto: "Contacto", Servicios: "Servicios", Registrate: "Registrate", Ingresar: "Ingresar", Pagina: "Pagina Principal", Que_Es: "¿Qué es?", Mision: "Misión", Vision: "Vision", Lideres: "Lideres", Ayuda: "Ayuda", Contactanos: "Contáctanos", Soporte:"Soporte", Creacion: "Creación de tickets",/*HOTBAR*/ Fecha: "Lun a Vie 8:00 am – 6:00 pm", Contactanos: "Contactanos", Footer: "© 2025–2025 GaiaLink: conecta, impulsa y transforma el futuro digital.", Privacidad: "Política de Privacidad", Terminos:"Términos y Condiciones"/*FOTTER*/},
        en: { BotonIdioma: "English" ,Inicio: "Start", Nosotros: "About us", Contacto: "Contact", Servicios: "Services", Registrate: "Sign Up", Ingresar: "Log In", Pagina: "Main Page", Que_Es: "What is it?", Mision: "Mission", Vision: "Vision", Lideres: "Leaders", Ayuda: "Help", Contactanos: "Contact us", Soporte:"Support", Creacion: "Ticket creation",/*HOTBAR*/ Fecha: "Mon to Fri 8:00 am – 6:00 pm", Contactanos: "Contact us", Footer: "© 2025–2025 GaiaLink: connect, drive, and transform the digital future.", Privacidad: "Privacy Policy", Terminos:"Terms and Conditions"/*FOTTER*/},
        fr: { BotonIdioma: "Français" ,Inicio: "Commencer", Nosotros: "À propos", Contacto: "Contact", Servicios: "Services", Registrate: "S'inscrire", Ingresar: "Connexion", Pagina: "Page principale", Que_Es: "Qu'est-ce que c'est ?", Mision: "Mission", Vision: "Vision", Lideres: "Leaders", Ayuda: "Aide", Contactanos: "Contactez-nous", Soporte:"Support", Creacion: "Création de tickets",/*HOTBAR*/ Fecha: "Lun à Ven 8h00 – 18h00", Contactanos: "Contactez-nous", Footer: "© 2025–2025 GaiaLink : connecte, stimule et transforme l’avenir numérique.", Privacidad: "Politique de confidentialité", Terminos:"Termes et conditions"/*FOTTER*/}
    };
    document.querySelectorAll("[data-lang]").forEach(el =>{
        const clave =  el.getAttribute("data-lang");
        el.textContent = traducciones[idioma][clave];
    });
    actualizarImagenIdioma(idioma);
    localStorage.setItem("idioma", idioma);
}
document.addEventListener("DOMContentLoaded", () => {
    const idiomaGuardado = localStorage.getItem("idioma") || "es";
    CambiarIdioma(idiomaGuardado);
});
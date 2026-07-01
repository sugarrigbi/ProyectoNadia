const API_BASE = 'https://bnstlf45-5000.use2.devtunnels.ms';
const BUCKET = 'https://gaialink.s3.us-east-1.amazonaws.com/';

function CambiarTema() {
    const Oscuro = document.body.classList.toggle("Modo_Oscuro");
    if (Oscuro) {
        localStorage.setItem("Tema", "Oscuro");
        document.getElementById("Cambiar_Tema_Texto").textContent = "Oscuro";
        document.getElementById("Cambiar_Tema_Imagen").src = "/Statics/img/Moon.svg"
        if (document.getElementById("Arrow_Usuario")){
            document.getElementById("Arrow_Usuario").src = "/Statics/img/Arrow_White.svg";           
            document.getElementById("Datos_Usuario").src = "/Statics/img/User_Claro.svg";                 
            document.getElementById("Ayuda_Usuario").src = "/Statics/img/Help_Claro.svg";                        
        }        
    } else {
        localStorage.setItem("Tema", "Claro");
        document.getElementById("Cambiar_Tema_Texto").textContent = "Claro";
        document.getElementById("Cambiar_Tema_Imagen").src = "/Statics/img/Sun.svg"            
    }
}
function Validar_Campos(Campos, Datos, Boton) {
    let Cambios = false;
    Campos.forEach(Campo =>{
        if (Campo.value !== Datos[Campo.name]){
            Cambios = true
        }
    });
    Boton.disabled = !Cambios
}

document.addEventListener("DOMContentLoaded", () => { 
    if (localStorage.getItem("Tema") === "Oscuro") {
        document.body.classList.add("Modo_Oscuro");
    }        
    const token = localStorage.getItem("Auth_Token") || sessionStorage.getItem("Auth_Token");
    if (!token) {
        window.location.href = "/login";
    }
    if (sessionStorage.getItem('caso_actualizado')) {
        sessionStorage.removeItem('caso_actualizado');

        Swal.fire({
            icon: 'success',
            title: 'Caso actualizado',
            text: 'Caso actualizado con éxito',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('caso_eliminado')) {
        sessionStorage.removeItem('caso_eliminado');

        Swal.fire({
            icon: 'error',
            title: 'Caso eliminado',
            text: 'El caso se eliminó correctamente',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('Relacion_Eliminada')) {
        sessionStorage.removeItem('Relacion_Eliminada');

        Swal.fire({
            icon: 'error',
            title: 'Relacion eliminada',
            text: 'La relacion se eliminó correctamente',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('Caso_Creado')) {
        sessionStorage.removeItem('Caso_Creado');

        Swal.fire({
            icon: 'success',
            title: 'Caso creado',
            text: 'Caso creado con éxito',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('Excel')) {
        sessionStorage.removeItem('Excel');

        Swal.fire({
            icon: 'success',
            title: 'Archivo descargado',
            text: 'Archivo descargado con éxito',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('Personal_Actualizado')) {
        sessionStorage.removeItem('Personal_Actualizado');

        Swal.fire({
            icon: 'success',
            title: 'Datos modificados',
            text: 'Datos modificados con éxito',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('dispositivo_eliminado')) {
        sessionStorage.removeItem('dispositivo_eliminado');

        Swal.fire({
            icon: 'error',
            title: 'Dispositivo eliminado',
            text: 'El dispositivo se eliminó correctamente',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    } 
    if (sessionStorage.getItem('MFA1')) {
        sessionStorage.removeItem('MFA1');

        Swal.fire({
            icon: 'success',
            title: 'Autenticacion activada',
            text: 'Autenticacion activada con éxito',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('MFA2')) {
        sessionStorage.removeItem('MFA2');

        Swal.fire({
            icon: 'error',
            title: 'Autenticacion desactivada',
            text: 'Autenticacion desactivada con éxito',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }
    if (sessionStorage.getItem('form_eliminado')) {
        sessionStorage.removeItem('form_eliminado');

        Swal.fire({
            icon: 'error',
            title: 'Formulario eliminado',
            text: 'El formulario se eliminó correctamente',
            timer: 2500,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
    }                
    
    window.addEventListener("popstate", () => {
        cargarPagina(window.location.pathname);
    });

    const Contenido = document.getElementById("contenido");
    const contenidoOriginal = Contenido.innerHTML; 

    function cargarPagina(url) {
        const Token_JWT = localStorage.getItem("Token_JWT");
        Contenido.innerHTML = contenidoOriginal;       
        fetch(url, {
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "Authorization": `Bearer ${Token_JWT}`
            }
        })
        .then(res => {
            if (res.status === 401){
                localStorage.removeItem("Token_JWT");
                localStorage.removeItem("User_Data"); 
                localStorage.removeItem("Auth_Token");
                sessionStorage.removeItem("Auth_Token");
                Swal.fire({
                    icon: 'warning',
                    title: 'Sesión expirada',
                    text: 'Debes iniciar sesión nuevamente',
                    timer: 2000,
                    showConfirmButton: false,
                    toast: true,
                    position: 'top-end',
                    background: '#1e1e2f',
                    color: '#ffffff',
                    iconColor: '#f1c40f',
                    width: '400px',
                    padding: '1.2rem',
                    customClass: {
                        popup: 'shadow-lg rounded-3'
                    }
                });              
                setTimeout(() => {
                    window.location.href = "/login";
                }, 2000);
                throw new Error("No autorizado");               
            }
            return res.text();
        })
        .then(html => {
            Contenido.innerHTML = html;
            history.pushState(null, "", url);
            const User = JSON.parse(localStorage.getItem("User_Data"));   
            if (localStorage.getItem("Tema") === "Oscuro") {
                document.body.classList.add("Modo_Oscuro");
                if (document.getElementById("Cambiar_Tema_Boton")){
                    document.getElementById("Cambiar_Tema_Imagen").src = "/Statics/img/Moon.svg";                    
                    document.getElementById("Cambiar_Tema_Texto").textContent = "Oscuro";
                }
                if (document.getElementById("Arrow_Usuario")){
                    document.getElementById("Arrow_Usuario").src = "/Statics/img/Arrow_White.svg";           
                    document.getElementById("Datos_Usuario").src = "/Statics/img/User_Claro.svg";                
                    document.getElementById("Ayuda_Usuario").src = "/Statics/img/Help_Claro.svg";                        
                }        
            } else {
                if (document.getElementById("Cambiar_Tema_Boton")){
                    document.getElementById("Cambiar_Tema_Texto").textContent = "Claro";
                    document.getElementById("Cambiar_Tema_Imagen").src = "/Statics/img/Sun.svg";
                }              
            }            
            if (document.getElementById("paginacion")){
                const paginacion = document.getElementById("paginacion")

                const Pag_Actual = Number(paginacion.dataset.actual)
                const Pag_Valida = Number(paginacion.dataset.validas)                

                const Pag_Ant2 = document.getElementById("Pag_Ant2");
                const Pag_Ant1 = document.getElementById("Pag_Ant1");
                const Pag_Act = document.getElementById("Pag_Act");
                const Pag_Sig1 = document.getElementById("Pag_Sig1");
                const Pag_Sig2 = document.getElementById("Pag_Sig2");
                const Pag_Sig3 = document.getElementById("Pag_Sig3");
                const Pag_Sig4 = document.getElementById("Pag_Sig4");

                const btn_prev = document.getElementById("btn-prev");
                const btn_next = document.getElementById("btn-next");

                if (Pag_Actual <= 1){
                    btn_prev.disabled = true
                }
                if (Pag_Actual >= Pag_Valida){
                    btn_next.disabled = true
                }
                
                btn_prev.addEventListener("click", () =>{
                    window.location = `?page=${Pag_Actual-1}`
                });
                btn_next.addEventListener("click", () =>{
                    window.location = `?page=${Pag_Actual+1}`
                });                

                if (Pag_Actual - 2 < 1){
                    Pag_Ant2.classList.add("d-none")
                    if (Pag_Actual + 3 <= Pag_Valida){
                        Pag_Sig3.classList.add("d-block")
                        Pag_Sig3.classList.remove("d-none")
                        Pag_Sig3.textContent = Pag_Actual + 3;
                        Pag_Sig3.href = `?page=${Pag_Actual + 3}`;                     
                    }
                } else {
                    Pag_Ant2.textContent = Pag_Actual - 2;
                    Pag_Ant2.href = `?page=${Pag_Actual - 2}`;
                }
                if (Pag_Actual - 1 < 1){
                    Pag_Ant1.classList.add("d-none");
                    if (Pag_Actual + 4 <= Pag_Valida){
                        Pag_Sig4.classList.add("d-block")
                        Pag_Sig4.classList.remove("d-none")
                        Pag_Sig4.textContent = Pag_Actual + 4;
                        Pag_Sig4.href = `?page=${Pag_Actual + 4}`;                  
                    }
                } else {
                    Pag_Ant1.textContent = Pag_Actual - 1;
                    Pag_Ant1.href = `?page=${Pag_Actual - 1}`;                
                } 
                
                if (Pag_Actual + 1 > Pag_Valida){
                    Pag_Sig1.classList.add("d-none")
                } else {
                    Pag_Sig1.textContent = Pag_Actual + 1
                    Pag_Sig1.href = `?page=${Pag_Actual + 1}`
                }
                if (Pag_Actual + 2 > Pag_Valida){
                    Pag_Sig2.classList.add("d-none")
                } else {
                    Pag_Sig2.textContent = Pag_Actual + 2
                    Pag_Sig2.href = `?page=${Pag_Actual + 2}`            
                }
            }                      
            if (document.getElementById("Nav_Casos_User")){
                const Nav_User = document.getElementById("Nav_Casos_User");
                const Nav_Admin = document.getElementById("Nav_Casos_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver")){
                    Nav_Admin.classList.remove("d-none");
                    Nav_Admin.classList.add("d-flex");                
                } else if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver_propio")){
                    Nav_User.classList.remove("d-none");
                    Nav_User.classList.add("d-flex");       
                }                         
            }
            if (document.getElementById("Card_Casos_User")){
                const Card_User = document.getElementById("Card_Casos_User");
                const Card_Admin = document.getElementById("Card_Casos_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver")){
                    Card_Admin.classList.remove("d-none");
                    Card_Admin.classList.add("d-flex");                    
                } else if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver_propio")){
                    Card_User.classList.remove("d-none");
                    Card_User.classList.add("d-flex");             
                }                         
            }                   
            if (document.getElementById("contenido")){
                const URL = window.location.pathname;
                const Boton_Crear = document.getElementById("Crear_Caso_Admin");
                const Form = document.getElementById("Caso_Contenedor");
                if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver")){
                    if (URL.includes("/user")){
                        cargarPagina("/dashboard/inicio");
                    }               
                } else if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver_propio")){                  
                    if (URL.includes("/staff")){
                        cargarPagina("/dashboard/inicio");
                    }
                }

                if (Boton_Crear) {
                    if (User.Permisos.some(Perm => Perm.Nombre === "caso_crear")){
                        Boton_Crear.classList.remove("d-none");
                        Boton_Crear.classList.add("d-flex");
                    }
                }
                if(Form){
                    if (!User.Permisos.some(Perm => Perm.Nombre === "caso_editar")){
                        Form.querySelectorAll("input, select, textarea").forEach(Input => {
                            Input.disabled = true;
                        });
                    }
                }
                document.querySelectorAll("[id^='Eliminar_Caso_Admin_']").forEach(Button => {
                    if (User.Permisos.some(Perm => Perm.Nombre === "caso_eliminar")){
                        Button.classList.remove("d-none");
                        Button.classList.add("d-flex");
                    }                    
                });
                document.querySelectorAll("[id^='Caso_Datos_']").forEach(div => {
                    const caso_id = div.dataset.caso;
                    const selectEstado = div.querySelector("select[name='Caso_Estado']");
                    const Input1 = div.querySelector("input[name='Caso_Direccion']");
                    const Input2 = div.querySelector("#barrio_input");
                    const Input3 = div.querySelector("#localidad_input");
                    const Input4 = div.querySelector("#ciudad_input");
                    const Input5 = div.querySelector("#departamento_input");
                    const InputComentario = div.querySelector("textarea[name='Caso_Comentario']");
                    const selecUserCargo = div.querySelector("select[name='Caso_Usuario_Cargo']");
                    const selecUserCreador = div.querySelector("select[name='Caso_Usuario_Creador']");
                    const Boton_Linea = div.querySelector(`button[data-button-id='${caso_id}']`);
                    if (!User.Permisos.some(Perm => Perm.Nombre === "caso_modificar_estado")){
                        selectEstado.disabled = true;
                    }
                    if (!User.Permisos.some(Perm => Perm.Nombre === "caso_modificar_direccion")){
                        Input1.disabled = true;
                        Input2.disabled = true;
                        Input3.disabled = true;
                        Input4.disabled = true;
                        Input5.disabled = true;
                    }
                    if (!User.Permisos.some(Perm => Perm.Nombre === "caso_asignar_usuario")){
                        selecUserCargo.disabled = true;
                        selecUserCreador.disabled = true;
                    }                    
                    if (!User.Permisos.some(Perm => Perm.Nombre === "caso_ver_linea_tiempo")){
                        Boton_Linea.classList.remove("d-flex");
                        Boton_Linea.classList.add("d-none");
                    }  
                    if (!User.Permisos.some(Perm => Perm.Nombre === "caso_comentar")){
                        InputComentario.disabled = true;
                    }                                         
                })                
            }            
            if (document.getElementById("User_Name")){
                document.getElementById("User_Name").textContent = User.User_Name;
            }            
            if (document.getElementById("User_Name2")){
                document.getElementById("User_Name2").textContent = User.User_Name;
            }      
            if (document.getElementById("User_Name3")){
                document.getElementById("User_Name3").textContent = User.User_Name;
            }
            if (document.getElementById("contenido")){
                document.querySelectorAll("[id^='User_Name_']").forEach(Name => {
                    Name.textContent = User.User_Name;
                })
                document.querySelectorAll("[id^='Imagen_Comentarios_']").forEach(Img_Com => {
                    const id = Img_Com.dataset.caso;
                    const Img_Error = document.getElementById(`Imagen_Error_${id}`);
                    const Nombre_Usuario = document.getElementById(`User_Name_${id}`).textContent.trim();
                    const GCS_URL = `${BUCKET}${User.Nombre_Imagen}`;

                    Img_Com.onerror = function(){
                        if (this.dataset.fallback !== "true"){
                            this.dataset.fallback = "true";
                            this.classList.add("d-none");
                            Img_Error.classList.remove("d-none");
                            Iniciales = Nombre_Usuario.slice(0, 2);
                            Img_Error.textContent = Iniciales;
                        }
                    };     
                    
                    Img_Com.src = `${GCS_URL}?_=${Date.now()}`;
                });                
            }                                   
            if(document.getElementById("Button_Cerrar")){
                document.getElementById("Button_Cerrar").addEventListener("click", () => {
                    localStorage.removeItem("Auth_Token")
                    sessionStorage.removeItem("Auth_Token")
                    window.location.href = "/login";
                })
            } 
            if (document.getElementById("Casos_Busqueda")) {
                document.querySelectorAll("#Casos_Busqueda span[id^='estado-span']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Pendiente") {
                        span.classList.add("estado-pendiente");
                    } else if (tipo === "Activo") {
                        span.classList.add("estado-activo");
                    } else if (tipo === "Resuelto") {
                        span.classList.add("estado-resuelto");
                    } else if (tipo === "Eliminado") {
                        span.classList.add("estado-eliminado");
                    } else if (tipo === "En espera del usuario") {
                        span.classList.add("estado-espera");
                    } else if (tipo === "Escalado a supervisor") {
                        span.classList.add("estado-escalado");
                    } else if (tipo === "Reabierto") {
                        span.classList.add("estado-reabierto");
                    } else if (tipo === "Tomando desicion "){
                        span.classList.add("estado-decision");
                    }
                });
                document.querySelectorAll("#Casos_Busqueda span[id^='prioridad-span']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Muy Baja"){
                        span.classList.add("prioridad-muy-baja");
                    }else if (tipo === "Baja"){
                        span.classList.add("prioridad-baja");
                    }else if (tipo === "Media"){
                        span.classList.add("prioridad-media");
                    }else if (tipo === "Alta"){
                        span.classList.add("prioridad-alta");
                    }else if (tipo === "Critica"){
                        span.classList.add("prioridad-critica");
                    }
                });
                document.querySelectorAll("#Casos_Busqueda span[id^='hora-span']").forEach(span => {
                    const raw = span.textContent.trim();
                    if (!raw) return;

                    const fecha = new Date(raw);
                    const ahora = new Date();
                    const diffMs = ahora - fecha;
                    const diffSec = Math.floor(diffMs / 1000);
                    const diffMin = Math.floor(diffSec / 60);
                    const diffHoras = Math.floor(diffMin / 60);
                    const diffDias = Math.floor(diffHoras / 24);

                    let texto;
                    if (diffMin < 60) {
                        texto = `hace ${diffMin} min${diffMin !== 1 ? 's' : ''}`;
                    } else if (diffHoras < 24) {
                        texto = `hace ${diffHoras} hora${diffHoras !== 1 ? 's' : ''}`;
                    } else if (diffDias <= 7) {
                        texto = `hace ${diffDias} día${diffDias !== 1 ? 's' : ''}`;
                    } else {
                        texto = fecha.toLocaleString("es-CO", {
                            day: "2-digit",
                            month: "2-digit",
                            year: "numeric",
                            hour: "2-digit",
                            minute: "2-digit"
                        });
                    }

                    span.textContent = texto;
                });     
                document.querySelectorAll("[id^='Fecha_Comentario_']").forEach(span => {
                    const raw = span.textContent.trim();
                    if (!raw) return;

                    const fechaLocal = new Date(raw);
                    const ahora = new Date();

                    const diffMs = ahora - fechaLocal;
                    const diffSec = Math.floor(diffMs / 1000);
                    const diffMin = Math.floor(diffSec / 60);
                    const diffHoras = Math.floor(diffMin / 60);
                    const diffDias = Math.floor(diffHoras / 24);

                    let texto;
                    if (diffMin < 60) {
                        texto = `hace ${diffMin} min${diffMin !== 1 ? 's' : ''}`;
                    } else if (diffHoras < 24) {
                        texto = `hace ${diffHoras} hora${diffHoras !== 1 ? 's' : ''}`;
                    } else if (diffDias <= 7) {
                        texto = `hace ${diffDias} día${diffDias !== 1 ? 's' : ''}`;
                    } else {
                        texto = fechaLocal.toLocaleString("es-CO", {
                            day: "2-digit",
                            month: "2-digit",
                            year: "numeric",
                            hour: "2-digit",
                            minute: "2-digit"
                        });
                    }

                    span.textContent = texto;
                });
                document.querySelectorAll("[id^='Fecha_Relacion']").forEach(span => {
                    const raw = span.textContent.trim();
                    if (!raw) return;

                    const fechaUTC = new Date(raw);
                    const fechaLocal = new Date(fechaUTC.getTime() + (5 * 60 * 60 * 1000));

                    const dia = String(fechaLocal.getDate()).padStart(2, '0');
                    const mes = String(fechaLocal.getMonth() + 1).padStart(2, '0');
                    const año = fechaLocal.getFullYear();

                    span.textContent = `${dia}/${mes}/${año}`;
                });
                document.querySelectorAll("[id^='Estado_Relacion_']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Pendiente") {
                        span.classList.add("estado-pendiente");
                    } else if (tipo === "Activo") {
                        span.classList.add("estado-activo");
                    } else if (tipo === "Resuelto") {
                        span.classList.add("estado-resuelto");
                    } else if (tipo === "Eliminado") {
                        span.classList.add("estado-eliminado");
                    } else if (tipo === "En espera del usuario") {
                        span.classList.add("estado-espera");
                    } else if (tipo === "Escalado a supervisor") {
                        span.classList.add("estado-escalado");
                    } else if (tipo === "Reabierto") {
                        span.classList.add("estado-reabierto");
                    } else if (tipo === "Tomando desicion "){
                        span.classList.add("estado-decision");
                    }
                });                
            }
            if (document.getElementById("contenido")){  
                if (document.getElementById("Imagen_Usuario_Crear")){
                    const img2 = document.getElementById("Imagen_Usuario_Crear")
                    const Img_Error = document.getElementById("Imagen_Error_Usuario_Crear");
                    const Nombre_Usuario = User.User_Name;
                    const GCS_URL = `${BUCKET}${User.Nombre_Imagen}`; 
                    
                    img2.onerror = function(){
                        if (this.dataset.fallback !== "true"){
                            this.dataset.fallback = "true";
                            this.classList.add("d-none");
                            Img_Error.classList.remove("d-none");
                            Iniciales = Nombre_Usuario.slice(0, 2);
                            Img_Error.textContent = Iniciales;                            
                        }
                    };      
                    
                    img2.src = `${GCS_URL}?_=${Date.now()}`;                    
                }
                document.querySelectorAll(".imagen_usuario").forEach(img =>{
                    const Nombre_Usuario = User.User_Name;
                    const Img_Error = img.nextElementSibling
                    const GCS_URL = `${BUCKET}${User.Nombre_Imagen}`;

                    img.onerror = function(){
                        if (this.dataset.fallback !== "true"){
                            this.dataset.fallback = "true";
                            this.classList.add("d-none");
                            Img_Error.classList.remove("d-none");
                            Iniciales = Nombre_Usuario.slice(0, 2);
                            Img_Error.textContent = Iniciales;
                        }
                    };      
                    
                    img.src = `${GCS_URL}?_=${Date.now()}`;
                });
                document.querySelectorAll("[id^='Imagen_Usuario_Comentario_']").forEach(Img_Com => {
                    const id = Img_Com.id.split("_").pop();
                    const Img_Error = Img_Com.nextElementSibling
                    const Nombre_Usuario = document.getElementById(`Obtener_Usuario_Comentario_${id}`).textContent.trim();
                    const GCS_URL = `${BUCKET}${User.Nombre_Imagen}`;

                    Img_Com.onerror = function(){
                        if (this.dataset.fallback !== "true"){
                            this.dataset.fallback = "true";
                            this.classList.add("d-none");
                            Img_Error.classList.remove("d-none");
                            Iniciales = Nombre_Usuario.slice(0, 2);
                            Img_Error.textContent = Iniciales;
                        }
                    };     
                    
                    Img_Com.src = `${GCS_URL}?_=${Date.now()}`;
                });
            }    
            if (document.getElementById("Caso_Contenedor")) {
                document.querySelectorAll("[id^='Caso_Botones_']").forEach(div => {
                    const caso_id = div.dataset.caso;
                    const Contenedor = document.getElementById(`Caso_Datos_${caso_id}`);
                    const Boton = document.getElementById(`Caso_Boton_Guardar_${caso_id}`);
                    const Boton2 = document.getElementById(`Caso_Boton_Recarga_${caso_id}`);
                    const Imagen = document.getElementById(`Caso_Boton_Guardar_Img_${caso_id}`);
                    const Campos = Array.from(Contenedor.querySelectorAll("input[name], select[name], textarea[name]"));
                    const inicial = new Map();
                    Campos.forEach((Campo, idx) => {
                        const tag = Campo.tagName.toLowerCase();
                        const type = (Campo.type || "").toLowerCase();
                        const key = Campo.name + "|" + idx;
                        if (type === "checkbox" || type === "radio") {
                            inicial.set(key, Campo.checked);
                        } else if (tag === "select" && Campo.multiple) {
                            inicial.set(key, Array.from(Campo.options).filter(o => o.selected).map(o => o.value).join("|"));
                        } else {
                            inicial.set(key, Campo.value);
                        }
                    });
                    function Hay_Cambios() {
                        for (let i = 0; i < Campos.length; i++) {
                        const Campo = Campos[i];
                        const tag = Campo.tagName.toLowerCase();
                        const type = (Campo.type || "").toLowerCase();
                        const key = Campo.name + "|" + i;

                        if (type === "checkbox" || type === "radio") {
                            if (inicial.get(key) !== Campo.checked) {
                                return true;
                            }
                        } else if (tag === "select" && Campo.multiple) {
                            const cur = Array.from(Campo.options).filter(o => o.selected).map(o => o.value).join("|");
                            if (inicial.get(key) !== cur){
                                return true;
                            }
                        } else {
                            if (inicial.get(key) !== Campo.value){
                                return true;
                            }
                        }
                        }
                        return false;
                    }          
                    function Si_Cambio() {
                        Boton.disabled = !Hay_Cambios();
                        if (Boton.disabled === false){
                            Boton2.disabled = false;
                            Boton2.classList.remove("boton9");
                            Boton2.classList.add("boton11");
                            Boton.classList.remove("text-black");
                            Boton.classList.add("text-info2");
                            Boton.classList.remove("boton9");
                            Boton.classList.add("boton10");
                            Imagen.src = "/Statics/img/Save.svg";
                        } else if (Boton.disabled === true){
                            Boton2.disabled = true;
                            Boton2.classList.add("boton9");
                            Boton2.classList.remove("boton11");                        
                            Boton.classList.add("text-black");
                            Boton.classList.remove("text-info2");
                            Boton.classList.add("boton9");
                            Boton.classList.remove("boton10");                        
                            Imagen.src = "/Statics/img/Save_2.svg";
                        }
                    } 
                    function restaurarCamposIniciales() {
                        if (!Campos || !inicial) return;
                        Campos.forEach((Campo, idx) => {
                            const tag = Campo.tagName.toLowerCase();
                            const type = (Campo.type || "").toLowerCase();
                            const key = Campo.name + "|" + idx;
                            const saved = inicial.get(key);

                            if (type === "checkbox" || type === "radio") {
                                Campo.checked = !!saved;
                            } else if (tag === "select" && Campo.multiple) {
                                const vals = (saved || "").split("|").filter(v => v !== "");
                                Array.from(Campo.options).forEach(opt => {
                                    opt.selected = vals.includes(opt.value);
                                });
                            } else if (tag === "select") {
                                if (saved !== undefined && saved !== null) {
                                    Campo.value = saved;
                                    if (Campo.value !== saved) Campo.selectedIndex = 0;
                                } else {
                                    Campo.selectedIndex = 0;
                                }
                            } else if (type === "file") {
                                Campo.value = null;
                            } else {
                                Campo.value = saved !== undefined && saved !== null ? saved : "";
                            }
                            Campo.dispatchEvent(new Event("input", { bubbles: true }));
                            Campo.dispatchEvent(new Event("change", { bubbles: true }));
                        });

                        if (typeof Si_Cambio === "function") Si_Cambio();
                    }
                    Campos.forEach(el => {
                        if (el.tagName.toLowerCase() === "select") {
                            el.addEventListener("change", Si_Cambio);
                        } else {
                            el.addEventListener("input", Si_Cambio);
                            el.addEventListener("change", Si_Cambio);
                        }
                    }); 
                    Boton.disabled = !Hay_Cambios();
                    if (Boton.disabled === false){
                        Boton2.disabled = false;
                        Boton2.classList.remove("boton9");
                        Boton2.classList.add("boton11");
                        Boton.classList.remove("text-black");
                        Boton.classList.add("text-info2");
                        Boton.classList.remove("boton9");
                        Boton.classList.add("boton10");
                        Imagen.src = "/Statics/img/Save.svg";
                    } else if (Boton.disabled === true){
                        Boton2.disabled = true;
                        Boton2.classList.add("boton9");
                        Boton2.classList.remove("boton11");                        
                        Boton.classList.add("text-black");
                        Boton.classList.remove("text-info2");
                        Boton.classList.add("boton9");
                        Boton.classList.remove("boton10");                        
                        Imagen.src = "/Statics/img/Save_2.svg";
                    }
                    Boton2.addEventListener("click", () =>{
                        restaurarCamposIniciales()
                    });                                                                    
                })
            }
            if (document.getElementById("Caso_Contenedor2")) {
                const Contenedor = document.getElementById("Caso_Contenedor2");
                const Boton = document.getElementById("CasoNuevo_Boton_Guardar");
                const Imagen = document.getElementById("CasoNuevo_Boton_Guardar_Img");
                const Campos = Array.from(Contenedor.querySelectorAll("input[name], select[name], textarea[name]"));
                const inicial = new Map();

                Campos.forEach((Campo, idx) => {
                    const tag = Campo.tagName.toLowerCase();
                    const type = (Campo.type || "").toLowerCase();
                    const key = Campo.name + "|" + idx;
                    if (type === "checkbox" || type === "radio") {
                        inicial.set(key, Campo.checked);
                    } else if (tag === "select" && Campo.multiple) {
                        inicial.set(key, Array.from(Campo.options).filter(o => o.selected).map(o => o.value).join("|"));
                    } else {
                        inicial.set(key, Campo.value);
                    }
                });
                function Hay_Cambios() {
                    for (let i = 0; i < Campos.length; i++) {
                    const Campo = Campos[i];
                    const tag = Campo.tagName.toLowerCase();
                    const type = (Campo.type || "").toLowerCase();
                    const key = Campo.name + "|" + i;

                    if (type === "checkbox" || type === "radio") {
                        if (inicial.get(key) !== Campo.checked) {
                            return true;
                        }
                    } else if (tag === "select" && Campo.multiple) {
                        const cur = Array.from(Campo.options).filter(o => o.selected).map(o => o.value).join("|");
                        if (inicial.get(key) !== cur){
                            return true;
                        }
                    } else {
                        if (inicial.get(key) !== Campo.value){
                            return true;
                        }
                    }
                    }
                    return false;
                }
                function Si_Cambio() {
                    Boton.disabled = !Hay_Cambios();
                    if (Boton.disabled === false){
                        Boton.classList.remove("text-black");
                        Boton.classList.add("text-info2");
                        Boton.classList.remove("boton9");
                        Boton.classList.add("boton10");
                        Imagen.src = "/Statics/img/Save.svg";
                    } else if (Boton.disabled === true){                     
                        Boton.classList.add("text-black");
                        Boton.classList.remove("text-info2");
                        Boton.classList.add("boton9");
                        Boton.classList.remove("boton10");                        
                        Imagen.src = "/Statics/img/Save_2.svg";
                    }
                }
                Campos.forEach(el => {
                    if (el.tagName.toLowerCase() === "select") {
                        el.addEventListener("change", Si_Cambio);
                    } else {
                        el.addEventListener("input", Si_Cambio);
                        el.addEventListener("change", Si_Cambio);
                    }
                });
                Boton.disabled = !Hay_Cambios();
                if (Boton.disabled === false){
                    Boton.classList.remove("text-black");
                    Boton.classList.add("text-info2");
                    Boton.classList.remove("boton9");
                    Boton.classList.add("boton10");
                    Imagen.src = "/Statics/img/Save.svg";
                } else if (Boton.disabled === true){                    
                    Boton.classList.add("text-black");
                    Boton.classList.remove("text-info2");
                    Boton.classList.add("boton9");
                    Boton.classList.remove("boton10");                        
                    Imagen.src = "/Statics/img/Save_2.svg";
                }
            }            
            if (document.getElementById("Caso_Contenedor")){
                document.getElementById("Caso_Contenedor").addEventListener("submit", async function(e){
                    e.preventDefault();
                    Id = document.getElementById("Obtener_Caso_Id").textContent.trim();
                    Boton = document.getElementById(`Caso_Boton_Guardar_${Id}`);
                    Boton_Mensaje = document.getElementById(`Caso_Boton_Guardar_Msg_${Id}`);
                    Boton.disabled = true;
                    Boton_Mensaje.textContent = "Guardando..."
                    document.getElementById(`div_Caso_Boton_Guardar_Img_${Id}`).innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#4674cb" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>'                    
                    document.getElementById("Caso_Boton_Volver").disabled = true
                    document.getElementById(`Caso_Boton_Recarga_${Id}`).disabled = true
                    document.getElementById(`Eliminar_Caso_Admin_${Id}`).disabled = true                      

                    const barrio_input = document.getElementById("barrio_input");
                    const barrio_input_nombre = document.getElementById("Caso_Barrio_Nombre");
                    const barrio_input_id = document.getElementById("Caso_Barrio_ID");
                    const barrio_datalist  = document.getElementById("Datalist_Barrio");

                    const localidad_input = document.getElementById("localidad_input");
                    const localidad_input_nombre = document.getElementById("Caso_Localidad_Nombre");
                    const localidad_input_id = document.getElementById("Caso_Localidad_ID");
                    const localidad_datalist  = document.getElementById("Datalist_Localidad");

                    const ciudad_input = document.getElementById("ciudad_input");
                    const ciudad_input_nombre = document.getElementById("Caso_Ciudad_Nombre");
                    const ciudad_input_id = document.getElementById("Caso_Ciudad_ID");
                    const ciudad_datalist  = document.getElementById("Datalist_Ciudad");

                    const departamento_input = document.getElementById("departamento_input");
                    const departamento_input_nombre = document.getElementById("Caso_Departamento_Nombre");
                    const departamento_input_id = document.getElementById("Caso_Departamento_ID");
                    const departamento_datalist  = document.getElementById("Datalist_Departamento");

                    const Update_Barrio = () => {
                        const Value = barrio_input.value.trim()
                        const Opcion = Array.from(barrio_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        barrio_input_nombre.value = Opcion ? Opcion.value : Value;
                        barrio_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : '';
                    }

                    const Update_Localidad = () => {
                        const Value = localidad_input.value.trim()
                        const Opcion = Array.from(localidad_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        localidad_input_nombre.value = Opcion ? Opcion.value : Value
                        localidad_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : ''
                    }

                    const Update_Ciudad = () => {
                        const Value = ciudad_input.value.trim()
                        const Opcion = Array.from(ciudad_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        ciudad_input_nombre.value = Opcion ? Opcion.value : Value
                        ciudad_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : ''
                    }

                    const Update_Departamento = () => {
                        const Value = departamento_input.value.trim()
                        const Opcion = Array.from(departamento_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        departamento_input_nombre.value = Opcion ? Opcion.value : Value
                        departamento_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : ''
                    }

                    barrio_input.addEventListener("input", Update_Barrio);
                    barrio_input.addEventListener("blur", Update_Barrio);
                    Update_Barrio()

                    localidad_input.addEventListener("input", Update_Localidad)
                    localidad_input.addEventListener("blur", Update_Localidad)
                    Update_Localidad()  

                    ciudad_input.addEventListener("input", Update_Ciudad)
                    ciudad_input.addEventListener("blur", Update_Ciudad)
                    Update_Ciudad()  
                    
                    departamento_input.addEventListener("input", Update_Departamento)
                    departamento_input.addEventListener("blur", Update_Departamento)
                    Update_Departamento()                    

                    const formData = new FormData(this);
                    const data = Object.fromEntries(formData.entries());

                    data.Caso_Id = Id;
                    data.Usuario_Id = User.User_ID;

                    data.Caso_Barrio = barrio_input_nombre.value
                    data.Caso_Barrio_ID = barrio_input_id.value

                    data.Caso_Localidad = localidad_input_nombre.value;
                    data.Caso_Localidad_ID = localidad_input_id.value;

                    data.Caso_Ciudad = ciudad_input_nombre.value;
                    data.Caso_Ciudad_ID = ciudad_input_id.value;

                    data.Caso_Departamento = departamento_input_nombre.value;
                    data.Caso_Departamento_ID = departamento_input_id.value;

                    const response = await fetch(`${API_BASE}/case/update/${Id}`, {method: "PUT", headers:{"Content-Type":"application/json", "Authorization": `Bearer ${Token_JWT}`},body: JSON.stringify(data)});
                    const result = await response.json()      
                    
                    if(response.status === 200){
                        sessionStorage.setItem('caso_actualizado', Id);                        
                        location.reload();
                    }
                    else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    }        
                    else if(response.status === 400){
                        window.scrollTo(0, 0);
                        Boton_Mensaje.textContent = result.Error;
                        Boton.classList.remove("boton9")
                        Boton.classList.add("boton8")
                        Boton.disabled = false;
                    }        
                    else if(response.status === 403){
                        document.body.classList.remove('modal-open');
                        document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
                        cargarPagina("/dashboard/unauthorized");
                    }                    
                });
            }   
            if (document.getElementById("SelectUsuario")) {
                const Select = document.getElementById("SelectUsuario");
                [...Select.options].forEach(opt => {
                if (opt.value !== String(User.User_ID)) {
                    opt.remove();
                } else {
                    opt.selected = true;
                }
                });
            }
            if (document.getElementById("Crear_Caso_User")){
                document.getElementById("Crear_Caso_User").addEventListener("submit", async function(e){
                    e.preventDefault();
                    
                    const Boton = document.getElementById("Crear_Caso_User_Boton");
                    Boton.disabled = true;

                    const Barrio_Input = document.getElementById("Barrio_Create");
                    const Barrio_Nombre = document.getElementById("Barrio_Create_Nombre");
                    const Barrio_ID = document.getElementById("Barrio_Create_ID");
                    const Barrio_Datalist = document.getElementById("Datalist_Barrio");   
                    const Update_Barrio = () => {
                        const Value = Barrio_Input.value.trim()
                        const Opcion = Array.from(Barrio_Datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())

                        Barrio_Nombre.value = Opcion ? Opcion.value : Value;
                        Barrio_ID.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : '';
                    }                                   

                    const Localidad_Input = document.getElementById("Localidad_Create");
                    const Localidad_Nombre = document.getElementById("Localidad_Create_Nombre");
                    const Localidad_ID = document.getElementById("Localidad_Create_ID");
                    const Localidad_Datalist = document.getElementById("Datalist_Localidad");
                    const Update_Localidad = () => {
                        const Value = Localidad_Input.value.trim();
                        const Opcion = Array.from(Localidad_Datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase());
                        Localidad_Nombre.value = Opcion ? Opcion.value : Value;
                        Localidad_ID.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : '';
                    }
                    
                    const Ciudad_Input = document.getElementById("Ciudad_Create");
                    const Ciudad_Nombre = document.getElementById("Ciudad_Create_Nombre");
                    const Ciudad_ID = document.getElementById("Ciudad_Create_ID");
                    const Ciudad_Datalist = document.getElementById("Datalist_Ciudad");
                    const Update_Ciudad = () => {
                        const Value = Ciudad_Input.value.trim();
                        const Opcion = Array.from(Ciudad_Datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase());
                        Ciudad_Nombre.value = Opcion ? Opcion.value : Value;
                        Ciudad_ID.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : '';
                    }                    
                    
                    const Departamento_Input = document.getElementById("Departamento_Create");
                    const Departamento_Nombre = document.getElementById("Departamento_Create_Nombre");
                    const Departamento_ID = document.getElementById("Departamento_Create_ID");  
                    const Departamento_Datalist = document.getElementById("Datalist_Departamento");                  
                    const Update_Departamento = () => {
                        const Value = Departamento_Input.value.trim();
                        const Opcion = Array.from(Departamento_Datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase());
                        Departamento_Nombre.value = Opcion ? Opcion.value : Value;
                        Departamento_ID.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : '';
                    }

                    Barrio_Input.addEventListener("input", Update_Barrio);
                    Barrio_Input.addEventListener("blur", Update_Barrio);
                    Update_Barrio()

                    Localidad_Input.addEventListener("input", Update_Localidad);
                    Localidad_Input.addEventListener("blur", Update_Localidad);
                    Update_Localidad();

                    Ciudad_Input.addEventListener("input", Update_Ciudad);
                    Ciudad_Input.addEventListener("blur", Update_Ciudad);
                    Update_Ciudad();

                    Departamento_Input.addEventListener("input", Update_Departamento);
                    Departamento_Input.addEventListener("blur", Update_Departamento);
                    Update_Departamento();

                    const formData = new FormData(this);
                    const data = Object.fromEntries(formData.entries());
                    
                    const response = await fetch(`${API_BASE}/case/create`, {method: "POST", headers:{"Content-Type":"application/json", "Authorization": `Bearer ${Token_JWT}`},body: JSON.stringify(data)});
                    const result = await response.json()
                    
                    if(response.status === 201){
                        sessionStorage.setItem('Caso_Creado', User.User_ID);                        
                        location.reload();
                    }
                    else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    }        
                    else if(response.status === 400){
                        window.scrollTo(0, 0);
                        Boton_Mensaje.textContent = result.Error;
                        Boton.classList.remove("boton9")
                        Boton.classList.add("boton8")
                        Boton.disabled = false;
                    }
                    else if(response.status === 403){
                        document.body.classList.remove('modal-open');
                        document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
                        cargarPagina("/dashboard/unauthorized");
                    }
                })
            }
            if (document.getElementById("Caso_Contenedor2")){
                document.getElementById("Caso_Contenedor2").addEventListener("submit", async function(e){
                    e.preventDefault();
                    Boton = document.getElementById("CasoNuevo_Boton_Guardar");
                    Boton_Mensaje = document.getElementById("CasoNuevo_Boton_Guardar_Msg");
                    Boton.disabled = true;
                    Boton_Mensaje.textContent = "Guardando..."
                    document.getElementById("div_CasoNuevo_Boton_Guardar_Img").innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#dfdfdf" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>'
                    document.getElementById("CasoNuevo_Boton_Volver").disabled = true                  

                    const barrio_input = document.getElementById("barrio_inputNuevo");
                    const barrio_input_nombre = document.getElementById("CasoNuevo_Barrio_Nombre");
                    const barrio_input_id = document.getElementById("CasoNuevo_Barrio_ID");
                    const barrio_datalist  = document.getElementById("Datalist_Barrio");

                    const localidad_input = document.getElementById("localidad_inputNuevo");
                    const localidad_input_nombre = document.getElementById("CasoNuevo_Localidad_Nombre");
                    const localidad_input_id = document.getElementById("CasoNuevo_Localidad_ID");
                    const localidad_datalist  = document.getElementById("Datalist_Localidad");

                    const ciudad_input = document.getElementById("ciudad_inputNuevo");
                    const ciudad_input_nombre = document.getElementById("CasoNuevo_Ciudad_Nombre");
                    const ciudad_input_id = document.getElementById("CasoNuevo_Ciudad_ID");
                    const ciudad_datalist  = document.getElementById("Datalist_Ciudad");

                    const departamento_input = document.getElementById("departamento_inputNuevo");
                    const departamento_input_nombre = document.getElementById("CasoNuevo_Departamento_Nombre");
                    const departamento_input_id = document.getElementById("CasoNuevo_Departamento_ID");
                    const departamento_datalist  = document.getElementById("Datalist_Departamento");

                    const Update_Barrio = () => {
                        const Value = barrio_input.value.trim()
                        const Opcion = Array.from(barrio_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        barrio_input_nombre.value = Opcion ? Opcion.value : Value;
                        barrio_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : '';
                    }

                    const Update_Localidad = () => {
                        const Value = localidad_input.value.trim()
                        const Opcion = Array.from(localidad_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        localidad_input_nombre.value = Opcion ? Opcion.value : Value
                        localidad_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : ''
                    }

                    const Update_Ciudad = () => {
                        const Value = ciudad_input.value.trim()
                        const Opcion = Array.from(ciudad_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        ciudad_input_nombre.value = Opcion ? Opcion.value : Value
                        ciudad_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : ''
                    }

                    const Update_Departamento = () => {
                        const Value = departamento_input.value.trim()
                        const Opcion = Array.from(departamento_datalist.options).find(opc => opc.value.toLowerCase() === Value.toLowerCase())
                        departamento_input_nombre.value = Opcion ? Opcion.value : Value
                        departamento_input_id.value = Opcion ? (Opcion.dataset.id || Opcion.getAttribute('data-id') || '') : ''
                    }

                    barrio_input.addEventListener("input", Update_Barrio);
                    barrio_input.addEventListener("blur", Update_Barrio);
                    Update_Barrio()

                    localidad_input.addEventListener("input", Update_Localidad)
                    localidad_input.addEventListener("blur", Update_Localidad)
                    Update_Localidad()  

                    ciudad_input.addEventListener("input", Update_Ciudad)
                    ciudad_input.addEventListener("blur", Update_Ciudad)
                    Update_Ciudad()  
                    
                    departamento_input.addEventListener("input", Update_Departamento)
                    departamento_input.addEventListener("blur", Update_Departamento)
                    Update_Departamento()                    

                    const formData = new FormData(this);
                    const data = Object.fromEntries(formData.entries());

                    data.Usuario_Id = User.User_ID;
                    
                    const response = await fetch(`${API_BASE}/case/create`, {method: "POST", headers:{"Content-Type":"application/json", "Authorization": `Bearer ${Token_JWT}`},body: JSON.stringify(data)});
                    const result = await response.json()
                    
                    if(response.status === 201){
                        sessionStorage.setItem('Caso_Creado', User.User_ID);                        
                        location.reload();
                    }
                    else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    }        
                    else if(response.status === 400){
                        window.scrollTo(0, 0);
                        Boton_Mensaje.textContent = result.Error;
                        Boton.classList.remove("boton9")
                        Boton.classList.add("boton8")
                        Boton.disabled = false;
                    }
                    else if(response.status === 403){
                        document.body.classList.remove('modal-open');
                        document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
                        cargarPagina("/dashboard/unauthorized");
                    }
                });
            }                    
            if (document.getElementById("Caso_Contenedor")){
                document.querySelectorAll("[id^='Caso_Boton_Eliminar_']").forEach(span => {
                    const caseId = span.dataset.caseId;
                    span.addEventListener("click", async (e) =>{
                        span.disabled = true;
                        const response = await fetch(`${API_BASE}/case/delete/${caseId}/${User.User_ID}`, {method: "PUT", headers:{"Authorization": `Bearer ${Token_JWT}`}});
                        const result = await response.json()     
                        
                        if(response.status === 200){
                            sessionStorage.setItem('caso_eliminado', caseId);                        
                            location.reload();
                        }
                        else if(response.status === 429){
                            window.location.href = "/rate-limit"
                        }        
                        else if(response.status === 400){
                            window.scrollTo(0, 0);
                            span.textContent = result.Error;
                        }      
                        else if(response.status === 403){
                            document.body.classList.remove('modal-open');
                            document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
                            cargarPagina("/dashboard/unauthorized");
                        }                                           
                    });
                });
                document.querySelectorAll("[id^='Boton_Relacion_']").forEach(el =>{
                    if (User.Permisos.some(Perm => Perm.Nombre === "caso_desrelacionar")){
                        el.classList.remove("d-none");
                        el.classList.add("d-flex");
                    }
                    el.addEventListener("click", async (e) =>{
                        el.disabled = true;
                        Rad_Padre = el.dataset.radPadre;
                        Rad_Hijo = el.dataset.radHijo;
                        Tipo_Relacion = el.dataset.radTipo;                        
                        const response = await fetch(`${API_BASE}/case/delete/relation/${Rad_Padre}/${Rad_Hijo}/${Tipo_Relacion}/${User.User_ID}`, {method: "DELETE"});
                        const result = await response.json()  

                        if(response.status === 200){
                            sessionStorage.setItem('Relacion_Eliminada', Rad_Padre);                        
                            location.reload();
                        }
                        else if(response.status === 429){
                            window.location.href = "/rate-limit"
                        }        
                        else if(response.status === 400){
                            window.scrollTo(0, 0);
                            span.textContent = result.Error;
                        }                            
                    });
                });
            }
            if (document.getElementById("Caso_Contenedor")){
                const estados = {
                    "Pendiente": "pendiente",
                    "Activo": "activo",
                    "Resuelto": "resuelto",
                    "Eliminado": "eliminado",
                    "En espera del usuario": "espera",
                    "Escalado a supervisor": "escalado",
                    "Reabierto": "reabierto",
                    "Tomando desicion": "decision"
                };                
                document.querySelectorAll("[id^='Abrir_Tiempo_']").forEach(Boton1 => {
                    const caseId = Boton1.dataset.buttonId;
                    const Boton2 = document.getElementById(`Abrir_Tiempo2_${caseId}`)
                    const Timeline = document.getElementById(`Timeline_${caseId}`);
                    Boton1.addEventListener("click", () =>{
                        Timeline.classList.remove("d-none");
                        Timeline.classList.add("d-flex");
                    });
                    Boton2.addEventListener("click", () =>{
                        Timeline.classList.remove("d-flex");
                        Timeline.classList.add("d-none");
                    });                    
                });
                document.querySelectorAll("[id^='Indentador_']").forEach(Cuadro => {
                    const Id = Cuadro.dataset.timeCard;

                    const Texto = document.getElementById(`Card_Texto_${Id}`)?.textContent.trim();
                    const Card = document.getElementById(`Card_Tiempo_${Id}`);
                    const LineaAbajo = document.getElementById(`Card_Linea_Abajo_${Id}`);
                    const LineaArriba = document.getElementById(`Card_Linea_Arriba_${Id}`);
                    const Circulo = document.getElementById(`Card_Circulo_${Id}`);

                    const estado = estados[Texto];

                    Card?.classList.add(`sombra-${estado}`);
                    LineaAbajo?.classList.add(`estado-${estado}2`);
                    LineaArriba?.classList.add(`estado-${estado}2`);
                    Circulo?.classList.add(`estado-${estado}2`);
                });                    
            }
            if (document.getElementById("Boton_Abrir_Filtro")){
                const BotonFiltro = document.getElementById("Boton_Abrir_Filtro");
                const BotonLimpiar = document.getElementById("Boton_Limpiar_Filtro");
                const BotonEnviar = document.getElementById("Boton_Enviar_Filtro");
                const Filtros = document.getElementById("Cont_Filtro");
                BotonFiltro.addEventListener("click", () =>{
                    if (Filtros.classList.contains("d-none")){
                        Filtros.classList.remove("d-none")
                        Filtros.classList.add("d-flex")
                    }else if (Filtros.classList.contains("d-flex")){
                        Filtros.classList.remove("d-flex")
                        Filtros.classList.add("d-none")
                    }
                });
                BotonLimpiar.addEventListener("click", () =>{
                    document.querySelectorAll("[id^='Check_Estado_']").forEach(CheckEstado => {
                        CheckEstado.checked = false;
                    });
                    document.querySelectorAll("[id^='Check_UsuarioEncargado_']").forEach(CheckUsuarioEncargado => {
                        CheckUsuarioEncargado.checked = false;
                    });
                    document.querySelectorAll("[id^='Check_UsuarioCreador_']").forEach(CheckUsuarioCreador => {
                        CheckUsuarioCreador.checked = false;
                    });
                    document.querySelectorAll("[id^='Check_Prioridad_']").forEach(CheckPrioridad => {
                        CheckPrioridad.checked = false;
                    });
                    document.querySelectorAll("[id^='Check_Incidente_']").forEach(CheckIncidente => {
                        CheckIncidente.checked = false;
                    });
                    document.getElementById("Check_Nombre").value = "";
                });
                BotonEnviar.addEventListener("click", () =>{
                    const Data = {
                        Estado: [],
                        Usuario_Encargado: [],
                        Usuario_Creador: [],
                        Prioridad: [],
                        Incidente: [],
                        Nombre: []
                    }

                    document.querySelectorAll("[id^='Check_Estado_']").forEach(CheckEstado => {
                        if (CheckEstado.checked){
                            Data.Estado.push(CheckEstado.value);
                        }
                    });
                    document.querySelectorAll("[id^='Check_UsuarioEncargado_']").forEach(CheckUsuarioEncargado => {
                        if (CheckUsuarioEncargado.checked){
                            Data.Usuario_Encargado.push(CheckUsuarioEncargado.value)
                        }
                    });
                    document.querySelectorAll("[id^='Check_UsuarioCreador_']").forEach(CheckUsuarioCreador => {
                        if (CheckUsuarioCreador.checked){
                            Data.Usuario_Creador.push(CheckUsuarioCreador.value)
                        }
                    });
                    document.querySelectorAll("[id^='Check_Prioridad_']").forEach(CheckPrioridad => {
                        if (CheckPrioridad.checked){
                            Data.Prioridad.push(CheckPrioridad.value)
                        }
                    });
                    document.querySelectorAll("[id^='Check_Incidente_']").forEach(CheckIncidente => {
                        if (CheckIncidente.checked){
                            Data.Incidente.push(CheckIncidente.value)
                        }
                    });   
                    if (document.getElementById("Check_Nombre").value !== ""){
                        Data.Nombre.push(document.getElementById("Check_Nombre").value)
                    }
                    const params = new URLSearchParams();
                    for (const key in Data) {
                        if (Array.isArray(Data[key])) {
                            Data[key].forEach(val => params.append(key, val));
                        } else {
                            params.append(key, Data[key]);
                        }
                    }
                    cargarPagina("/dashboard/staff/casos/search?" + params.toString());
                });
            }
            if (document.getElementById("Caso_Contenedor")){
                const botones = document.querySelectorAll(".Agregar_Trabajo");
                botones.forEach(boton => {
                    const Mensaje_Boton = boton.querySelector(".Agregar_Trabajo_Mensaje");
                    const Imagen_Boton = boton.querySelector(".Agregar_Trabajo_Imagen");
                    const casoId = boton.dataset.caso; 
                    const card = document.querySelector(`.Crear_Relacion[data-caso='${casoId}']`);
                    if (User.Permisos.some(Perm => Perm.Nombre === "caso_relacionar")){
                        boton.classList.remove("d-none");
                        boton.classList.add("d-flex");
                    }                    
                    boton.addEventListener("click", () => {           
                        const selectTipo = card.querySelector(".Relacion_Tipo");
                        const selectRadicado = card.querySelector(".Relacion_Radicado");                           
                        if (card.classList.contains("d-none")) {
                            card.classList.remove("d-none");
                            card.classList.add("d-flex");
                            Mensaje_Boton.textContent = "Eliminar trabajo";
                            Imagen_Boton.src = "/Statics/img/Minus.svg";
                            selectTipo.required = true;
                            selectRadicado.required = true;
                        }else if (!card.classList.contains("d-none")){                                                     
                            selectTipo.selectedIndex = 0;
                            selectRadicado.selectedIndex = 0;
                            selectTipo.required = false;
                            selectRadicado.required = false;                        
                            Mensaje_Boton.textContent = "Añadir trabajo";
                            Imagen_Boton.src = "/Statics/img/Plus.svg";
                            card.classList.remove("d-flex");
                            card.classList.add("d-none");
                        }
                    });
                });
            } 
            if (document.getElementById("Agregar_Trabajo")){
                const Boton = document.getElementById("Agregar_Trabajo");
                const Mensaje = document.getElementById("Agregar_Trabajo_Mensaje");
                const Imagen = document.getElementById("Agregar_Trabajo_Imagen");
                const Card = document.getElementById("Crear_Relacion");
                Boton.addEventListener("click", () =>{
                    if (Card.classList.contains("d-none")){
                        Card.classList.remove("d-none")
                        Card.classList.add("d-flex")
                        Mensaje.textContent = "Eliminar trabajo";
                        Imagen.src = "/Statics/img/Minus.svg";
                        document.getElementById("Relacion_Tipo").required = true;
                        document.getElementById("Relacion_Radicado").required = true;
                    }else if (Card.classList.contains("d-flex")){
                        Card.classList.remove("d-flex")
                        Card.classList.add("d-none")
                        document.getElementById("Relacion_Radicado").selectedIndex = 0;
                        document.getElementById("Relacion_Radicado").required = false;                        
                        document.getElementById("Relacion_Tipo").selectedIndex = 0;
                        document.getElementById("Relacion_Tipo").required = false;
                        Mensaje.textContent = "Añadir trabajo";
                        Imagen.src = "/Statics/img/Plus.svg";                        
                    }
                })
            }   
            if (document.getElementById("Casos_User")) {
                document.querySelectorAll("#Casos_User span[id^='estado-span-']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Pendiente") {
                        span.classList.add("estado-pendiente");
                    } else if (tipo === "Activo") {
                        span.classList.add("estado-activo");
                    } else if (tipo === "Resuelto") {
                        span.classList.add("estado-resuelto");
                    } else if (tipo === "Eliminado") {
                        span.classList.add("estado-eliminado");
                    } else if (tipo === "En espera del usuario") {
                        span.classList.add("estado-espera");
                    } else if (tipo === "Escalado a supervisor") {
                        span.classList.add("estado-escalado");
                    } else if (tipo === "Reabierto") {
                        span.classList.add("estado-reabierto");
                    } else if (tipo === "Tomando desicion "){
                        span.classList.add("estado-decision");
                    }
                });
                document.querySelectorAll("#Casos_User span[id^='estado-span2-']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Pendiente") {
                        span.classList.add("estado-pendiente");
                    } else if (tipo === "Activo") {
                        span.classList.add("estado-activo");
                    } else if (tipo === "Resuelto") {
                        span.classList.add("estado-resuelto");
                    } else if (tipo === "Eliminado") {
                        span.classList.add("estado-eliminado");
                    } else if (tipo === "En espera del usuario") {
                        span.classList.add("estado-espera");
                    } else if (tipo === "Escalado a supervisor") {
                        span.classList.add("estado-escalado");
                    } else if (tipo === "Reabierto") {
                        span.classList.add("estado-reabierto");
                    } else if (tipo === "Tomando desicion "){
                        span.classList.add("estado-decision");
                    }
                });                
                document.querySelectorAll("#Casos_Busqueda span[id^='prioridad-span']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Muy Baja"){
                        span.classList.add("prioridad-muy-baja");
                    }else if (tipo === "Baja"){
                        span.classList.add("prioridad-baja");
                    }else if (tipo === "Media"){
                        span.classList.add("prioridad-media");
                    }else if (tipo === "Alta"){
                        span.classList.add("prioridad-alta");
                    }else if (tipo === "Critica"){
                        span.classList.add("prioridad-critica");
                    }
                });               
            }   
            if (document.getElementById("Entidad_Contenedor")) {
                document.querySelectorAll("span[id^='estado-span-']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Activa") {
                        span.classList.add("estado-activo");
                    } else if (tipo === "Inactiva") {
                        span.classList.add("estado-eliminado");
                    } else if (tipo === "Suspendida") {
                        span.classList.add("estado-espera");
                    } else if (tipo === "Eliminada") {
                        span.classList.add("estado-escalado");
                    }
                });  
            }          
            if (document.getElementById("Entidad_Contenedor")) {
                document.querySelectorAll("span[id^='incidente-span-']").forEach(span => {
                    const tipo = span.textContent.trim();
                    if (tipo === "Desplazamiento") {
                        span.classList.add("estado-pendiente");
                    } else if (tipo === "Predios Despojados") {
                        span.classList.add("estado-eliminado");
                    } else if (tipo === "Expropiacion") {
                        span.classList.add("estado-decision");
                    } else if (tipo === "Hurto") {
                        span.classList.add("estado-escalado");
                    }
                });  
            }          
            if (document.getElementById("Boton_Abrir_Filtro2")){
                const BotonFiltro = document.getElementById("Boton_Abrir_Filtro2");
                const BotonLimpiar = document.getElementById("Boton_Limpiar_Filtro2");
                const BotonEnviar = document.getElementById("Boton_Enviar_Filtro2");
                const Filtros = document.getElementById("Cont_Filtro2");
                BotonFiltro.addEventListener("click", () =>{
                    if (Filtros.classList.contains("d-none")){
                        Filtros.classList.remove("d-none")
                        Filtros.classList.add("d-flex")
                    }else if (Filtros.classList.contains("d-flex")){
                        Filtros.classList.remove("d-flex")
                        Filtros.classList.add("d-none")
                    }
                });
                BotonLimpiar.addEventListener("click", () =>{
                    document.querySelectorAll("[id^='Check_Estado_']").forEach(CheckEstado => {
                        CheckEstado.checked = false;
                    });
                    document.querySelectorAll("[id^='Check_Incidente_']").forEach(CheckIncidente => {
                        CheckIncidente.checked = false;
                    });
                    document.getElementById("Check_Nombre").value = "";
                });
                BotonEnviar.addEventListener("click", () =>{
                    const Data = {
                        Estado: [],
                        Incidente: [],
                        Nombre: []
                    }

                    document.querySelectorAll("[id^='Check_Estado_']").forEach(CheckEstado => {
                        if (CheckEstado.checked){
                            Data.Estado.push(CheckEstado.value);
                        }
                    });
                    document.querySelectorAll("[id^='Check_Incidente_']").forEach(CheckIncidente => {
                        if (CheckIncidente.checked){
                            Data.Incidente.push(CheckIncidente.value)
                        }
                    });   
                    if (document.getElementById("Check_Nombre").value !== ""){
                        Data.Nombre.push(document.getElementById("Check_Nombre").value)
                    }
                    const params = new URLSearchParams();
                    for (const key in Data) {
                        if (Array.isArray(Data[key])) {
                            Data[key].forEach(val => params.append(key, val));
                        } else {
                            params.append(key, Data[key]);
                        }
                    }
                    cargarPagina("/dashboard/staff/entidades/search?" + params.toString());
                });
            }
            if (document.getElementById("contenido")){
                const URL = window.location.pathname;
                const Boton_Crear = document.getElementById("Crear_Entidad_Admin");
                const Form = document.getElementById("Entidad_Contenedor");
                if (!User.Permisos.some(Perm => Perm.Nombre === "entidad_ver")){
                    if (URL.includes("/entidades")){
                        cargarPagina("/dashboard/inicio");
                    }            
                }
                if (Boton_Crear) {
                    if (User.Permisos.some(Perm => Perm.Nombre === "entidad_crear")){
                        Boton_Crear.classList.remove("d-none");
                        Boton_Crear.classList.add("d-flex");
                    }
                }
                if(Form){
                    if (!User.Permisos.some(Perm => Perm.Nombre === "entidad_editar")){
                        Form.querySelectorAll("input, select, textarea").forEach(Input => {
                            Input.disabled = true;
                        });
                    }
                }
                document.querySelectorAll("[id^='Eliminar_Entidad_Admin_']").forEach(Button => {
                    if (User.Permisos.some(Perm => Perm.Nombre === "entidad_eliminar")){
                        Button.classList.remove("d-none");
                        Button.classList.add("d-flex");
                    }                    
                });               
            }   
            if (document.getElementById("Entidad_Contenedor")) {
                document.querySelectorAll("[id^='Entidad_Botones_']").forEach(div => {
                    const entidad_id = div.dataset.entidad;
                    const Contenedor = document.getElementById(`Entidad_Datos_${entidad_id}`);
                    const Boton = document.getElementById(`Entidad_Boton_Guardar_${entidad_id}`);
                    const Boton2 = document.getElementById(`Entidad_Boton_Recarga_${entidad_id}`);
                    const Imagen = document.getElementById(`Entidad_Boton_Guardar_Img_${entidad_id}`);
                    const Campos = Array.from(Contenedor.querySelectorAll("input[name], select[name], textarea[name]"));
                    const inicial = new Map();

                    Campos.forEach((Campo, idx) => {
                        const key = Campo.name + "|" + idx;
                        if (Campo.tagName.toLowerCase() === "select" && Campo.multiple) {
                            inicial.set(key, Array.from(Campo.options).filter(o => o.selected).map(o => o.value).join("|"));
                        } else {
                            inicial.set(key, Campo.value);
                        }
                    });

                    function Hay_Cambios() {
                        for (let i = 0; i < Campos.length; i++) {
                            const Campo = Campos[i];
                            const key = Campo.name + "|" + i;
                            if (Campo.tagName.toLowerCase() === "select" && Campo.multiple) {
                                const cur = Array.from(Campo.options).filter(o => o.selected).map(o => o.value).join("|");
                                if (inicial.get(key) !== cur) return true;
                            } else {
                                if (inicial.get(key) !== Campo.value) return true;
                            }
                        }
                        return false;
                    }

                    function Si_Cambio() {
                        Boton.disabled = !Hay_Cambios();
                        if (!Boton.disabled) {
                            Boton2.disabled = false;
                            Boton2.classList.replace("boton9", "boton11");
                            Boton.classList.replace("boton9", "boton10");
                            Boton.classList.replace("text-black", "text-info2");
                            Imagen.src = "/Statics/img/Save.svg";
                        } else {
                            Boton2.disabled = true;
                            Boton2.classList.replace("boton11", "boton9");
                            Boton.classList.replace("boton10", "boton9");
                            Boton.classList.replace("text-info2", "text-black");
                            Imagen.src = "/Statics/img/Save_2.svg";
                        }
                    }

                    function restaurarCamposIniciales() {
                        Campos.forEach((Campo, idx) => {
                            const key = Campo.name + "|" + idx;
                            const saved = inicial.get(key);
                            if (Campo.tagName.toLowerCase() === "select" && Campo.multiple) {
                                const vals = (saved || "").split("|").filter(v => v !== "");
                                Array.from(Campo.options).forEach(opt => { opt.selected = vals.includes(opt.value); });
                            } else if (Campo.tagName.toLowerCase() === "select") {
                                Campo.value = saved;
                                if (Campo.value !== saved) Campo.selectedIndex = 0;
                            } else {
                                Campo.value = saved !== undefined && saved !== null ? saved : "";
                            }
                            Campo.dispatchEvent(new Event("input", { bubbles: true }));
                            Campo.dispatchEvent(new Event("change", { bubbles: true }));
                        });
                        Si_Cambio();
                    }

                    Campos.forEach(el => {
                        el.addEventListener(el.tagName.toLowerCase() === "select" ? "change" : "input", Si_Cambio);
                        el.addEventListener("change", Si_Cambio);
                    });
                    Boton2.addEventListener("click", restaurarCamposIniciales);
                    Si_Cambio();
                });
                document.getElementById("Entidad_Contenedor").addEventListener("submit", async function (e) {
                    e.preventDefault();
                    const Boton = document.querySelector("[id^='Entidad_Boton_Guardar_']:not(:disabled)") || e.submitter;
                    const entidad_id = document.querySelector("[id^='Obtener_Entidad_Id_']")?.textContent.trim();
                    const Boton_Mensaje = document.getElementById(`Entidad_Boton_Guardar_Msg_${entidad_id}`);
                    if (Boton) Boton.disabled = true;

                    const formData = new FormData(this);
                    const data = Object.fromEntries(formData.entries());
                    data.Entidad_Id = entidad_id;

                    const response = await fetch(`${API_BASE}/entity/update/${entidad_id}`, {
                        method: "PUT",
                        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${Token_JWT}` },
                        body: JSON.stringify(data)
                    });
                    const result = await response.json();

                    if (response.status === 200) {
                        sessionStorage.setItem('entidad_actualizada', entidad_id);
                        location.reload();
                    } else if (response.status === 429) {
                        window.location.href = "/rate-limit";
                    } else if (response.status === 400) {
                        window.scrollTo(0, 0);
                        if (Boton_Mensaje) Boton_Mensaje.textContent = result.Error;
                        if (Boton) Boton.disabled = false;
                    } else if (response.status === 403) {
                        document.body.classList.remove('modal-open');
                        document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
                        cargarPagina("/dashboard/unauthorized");
                    }
                });
                document.querySelectorAll("[id^='Entidad_Boton_Eliminar_']").forEach(span => {
                    const entidadId = span.dataset.entidadId;
                    span.addEventListener("click", async () => {
                        span.disabled = true;
                        const response = await fetch(`${API_BASE}/entity/delete/${entidadId}`, {
                            method: "PUT",
                            headers: { "Authorization": `Bearer ${Token_JWT}` }
                        });
                        const result = await response.json();

                        if (response.status === 200) {
                            sessionStorage.setItem('entidad_eliminada', entidadId);
                            location.reload();
                        } else if (response.status === 429) {
                            window.location.href = "/rate-limit";
                        } else if (response.status === 403) {
                            document.body.classList.remove('modal-open');
                            document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
                            cargarPagina("/dashboard/unauthorized");
                        } else {
                            span.disabled = false;
                        }
                    });
                });
            }
            if (document.getElementById("Entidad_Contenedor2")) {
                const Contenedor = document.getElementById("Entidad_Contenedor2");
                const Boton = document.getElementById("EntidadNueva_Boton_Guardar");
                const Imagen = document.getElementById("EntidadNueva_Boton_Guardar_Img");
                const Campos = Array.from(Contenedor.querySelectorAll("input[name], select[name], textarea[name]"));
                const inicial = new Map();

                Campos.forEach((Campo, idx) => {
                    inicial.set(Campo.name + "|" + idx, Campo.value);
                });

                function Hay_Cambios_Nuevo() {
                    for (let i = 0; i < Campos.length; i++) {
                        if (inicial.get(Campos[i].name + "|" + i) !== Campos[i].value) return true;
                    }
                    return false;
                }

                function Si_Cambio_Nuevo() {
                    Boton.disabled = !Hay_Cambios_Nuevo();
                    if (!Boton.disabled) {
                        Boton.classList.replace("boton9", "boton10");
                        Boton.classList.replace("text-black", "text-info2");
                        Imagen.src = "/Statics/img/Save.svg";
                    } else {
                        Boton.classList.replace("boton10", "boton9");
                        Boton.classList.replace("text-info2", "text-black");
                        Imagen.src = "/Statics/img/Save_2.svg";
                    }
                }

                Campos.forEach(el => {
                    el.addEventListener(el.tagName.toLowerCase() === "select" ? "change" : "input", Si_Cambio_Nuevo);
                    el.addEventListener("change", Si_Cambio_Nuevo);
                });
                Si_Cambio_Nuevo();

                Contenedor.addEventListener("submit", async function (e) {
                    e.preventDefault();
                    Boton.disabled = true;
                    const Boton_Mensaje = document.getElementById("EntidadNueva_Boton_Guardar_Msg");

                    const formData = new FormData(this);
                    const data = Object.fromEntries(formData.entries());

                    const response = await fetch(`${API_BASE}/entity/create`, {
                        method: "POST",
                        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${Token_JWT}` },
                        body: JSON.stringify(data)
                    });
                    const result = await response.json();

                    if (response.status === 201) {
                        sessionStorage.setItem('entidad_creada', 'true');
                        location.reload();
                    } else if (response.status === 429) {
                        window.location.href = "/rate-limit";
                    } else if (response.status === 400) {
                        window.scrollTo(0, 0);
                        Boton_Mensaje.textContent = result.Error;
                        Boton.classList.replace("boton9", "boton8");
                        Boton.disabled = false;
                    } else if (response.status === 403) {
                        document.body.classList.remove('modal-open');
                        document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
                        cargarPagina("/dashboard/unauthorized");
                    }
                });
            }
            if (document.getElementById("Nav_Entidades_Admin")){
                const Nav_Entidad = document.getElementById("Nav_Entidades_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "entidad_ver")){
                    Nav_Entidad.classList.remove("d-none");
                    Nav_Entidad.classList.add("d-flex");                
                }                         
            }
            if (document.getElementById("Card_Entidades_Admin")){
                const Card_Entidades = document.getElementById("Card_Entidades_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "entidad_ver")){
                    Card_Entidades.classList.remove("d-none");
                    Card_Entidades.classList.add("d-flex");                    
                }                       
            }
            if (document.getElementById("Health_Cards")){
                if (document.getElementById("Card_Estado_API")){
                    const Card = document.getElementById("Card_Estado_API");
                    const Imagen = document.getElementById("Fondo_Imagen_API");
                    const Estado = document.getElementById("Dato_Estado_API").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/API_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/API_OK.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }
                if (document.getElementById("Card_Estado_Account")){
                    const Card = document.getElementById("Card_Estado_Account");
                    const Imagen = document.getElementById("Fondo_Imagen_Account");
                    const Estado = document.getElementById("Dato_Estado_Account").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/Account_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/Account_OFF.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }
                if (document.getElementById("Card_Estado_Authenticator")){
                    const Card = document.getElementById("Card_Estado_Authenticator");
                    const Imagen = document.getElementById("Fondo_Imagen_Authenticator");
                    const Estado = document.getElementById("Dato_Estado_Authenticator").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/Authenticator_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/Authenticator_OFF.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }
                if (document.getElementById("Card_Estado_Case")){
                    const Card = document.getElementById("Card_Estado_Case");
                    const Imagen = document.getElementById("Fondo_Imagen_Case");
                    const Estado = document.getElementById("Dato_Estado_Case").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/Case_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/Case_OFF.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }
                if (document.getElementById("Card_Estado_Entity")){
                    const Card = document.getElementById("Card_Estado_Entity");
                    const Imagen = document.getElementById("Fondo_Imagen_Entity");
                    const Estado = document.getElementById("Dato_Estado_Entity").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/Entity_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/Entity_OFF.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }
                if (document.getElementById("Card_Estado_Forms")){
                    const Card = document.getElementById("Card_Estado_Forms");
                    const Imagen = document.getElementById("Fondo_Imagen_Forms");
                    const Estado = document.getElementById("Dato_Estado_Forms").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/Forms_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/Forms_OFF.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }
                if (document.getElementById("Card_Estado_Notification")){
                    const Card = document.getElementById("Card_Estado_Notification");
                    const Imagen = document.getElementById("Fondo_Imagen_Notification");
                    const Estado = document.getElementById("Dato_Estado_Notification").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/Notification_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/Notification_OFF.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }
                if (document.getElementById("Card_Estado_User")){
                    const Card = document.getElementById("Card_Estado_User");
                    const Imagen = document.getElementById("Fondo_Imagen_User");
                    const Estado = document.getElementById("Dato_Estado_User").textContent.trim();
                    if (Estado === "OK"){
                        Imagen.classList.add("Bg_OK");
                        Imagen.src = "/Statics/img/User_OK.svg";
                        Card.classList.add("Bg_OK2")
                        Card.classList.add("Border_OK")
                    } else if (Estado === "OFF"){
                        Imagen.classList.add("Bg_OFF");
                        Imagen.src = "/Statics/img/User_OFF.svg";
                        Card.classList.add("Bg_OFF2")
                        Card.classList.add("Border_OFF")
                    }
                }                
            }     
            if (document.getElementById("Health_Cards")){
                const URL = window.location.pathname;
                if (!User.Permisos.some(Perm => Perm.Nombre === "health_check")){
                    if (URL.includes("/staff")){
                        cargarPagina("/dashboard/inicio");
                    }
                }
            }
            if (document.getElementById("Card_Health_Admin")){
                const Card_Health = document.getElementById("Card_Health_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "health_check")){
                    Card_Health.classList.remove("d-none");
                    Card_Health.classList.add("d-flex");                    
                }                       
            }        
            if (document.getElementById("Nav_Health_Admin")){
                const Nav_Entidad = document.getElementById("Nav_Health_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "health_check")){
                    Nav_Entidad.classList.remove("d-none");
                    Nav_Entidad.classList.add("d-flex");                
                }                         
            }    
            if (document.getElementById("Ultimo_Uso_Device")){
                document.querySelectorAll("#Ultimo_Uso_Device").forEach(el => {
                    const raw = el.textContent.trim();
                    const date = new Date(raw);
                    const now = new Date();
                    const diff = Math.floor((now - date) / 1000);

                    let texto;

                    if (diff < 60) {
                        texto = "hace un momento";
                    } else if (diff < 3600) {
                        const mins = Math.floor(diff / 60);
                        texto = `hace ${mins} minuto${mins > 1 ? "s" : ""}`;
                    } else if (diff < 86400) {
                        const horas = Math.floor(diff / 3600);
                        texto = `hace ${horas} hora${horas > 1 ? "s" : ""}`;
                    } else if (diff < 2592000) {
                        const dias = Math.floor(diff / 86400);
                        texto = `hace ${dias} día${dias > 1 ? "s" : ""}`;
                    } else {
                        texto = date.toLocaleDateString("es-CO", { day: "2-digit", month: "2-digit", year: "numeric" });
                    }

                    el.textContent = texto;
                });
            } 
            if (document.getElementById("Devices_Cards")){
                document.querySelectorAll(".Imagen_Device").forEach(Imagen => {
                    const Valor = Imagen.getAttribute("data-type");
                    if (Valor === "Computador"){
                        Imagen.src = "/Statics/img/Computador_Device.svg";
                    } else if (Valor === "Móvil"){
                        Imagen.src = "/Statics/img/Celular_Device.svg";
                    } else if (Valor === "Tablet"){
                        Imagen.src = "/Statics/img/Tablet_Device.svg";
                    } else if (Valor === "Desconocido"){
                        Imagen.src = "/Statics/img/Desconocido_Device.svg";
                    }
                })
            }   
            if (document.getElementById("Cont_Cuenta")){
                document.querySelectorAll(".Boton_Eliminar_Device").forEach(Button =>{
                    const Ant = Button.innerHTML
                    const Device_ID = Button.getAttribute("data-delete");
                    const Token = Button.getAttribute("data-token");
                    if (!User.Permisos.some(Perm => Perm.Nombre === "dispositivo_eliminar")){
                        Button.classList.add("d-none");
                    }
                    Button.addEventListener("click", async (e) =>{
                        Button.disabled = true;
                        Button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Eliminando...'
                        const response = await fetch(`${API_BASE}/device/delete/${Device_ID}`, {method: "PUT", headers:{"Authorization": `Bearer ${Token_JWT}`}});
                        const result = await response.json()
                        if(response.status === 200){
                            if(localStorage.getItem("Device_Token") === Token){
                                localStorage.removeItem("Auth_Token")
                                localStorage.removeItem("Device_Token")
                                sessionStorage.removeItem("Auth_Token")
                                window.location.href = "/login";
                            }
                            sessionStorage.setItem('dispositivo_eliminado', Device_ID);
                            location.reload();
                        } else if(response.status === 429){
                            window.location.href = "/rate-limit"
                        } else if(response.status === 400){
                            Button.innerHTML = Ant
                            Button.disabled = false;
                            Button.textContent = result.Error;
                        } else if(response.status === 403){
                            cargarPagina("/dashboard/unauthorized");
                        }                                                               
                    })
                })
            }
            if (document.getElementById("Cambiar_Mfa")){
                const Boton = document.getElementById("Cambiar_Mfa");
                const Ant = Boton.innerHTML
                const Mensaje = document.getElementById("Mensaje_Mfa2");
                const Dato = document.getElementById("Mensaje_Mfa");
                if (Dato.textContent.trim() === "False"){
                    Boton.textContent = "Activar"
                    Boton.classList.add("Bg_OK3")
                    Boton.classList.add("boton17")
                    Mensaje.textContent = "Desactivada"
                } else if (Dato.textContent.trim() === "True"){
                    Boton.textContent = "Desactivar"
                    Boton.classList.add("Bg_OFF3")
                    Boton.classList.add("boton8")
                    Mensaje.textContent = "Activada"
                }                

                Boton.addEventListener("click", async (e) =>{
                    if (Dato.textContent.trim() === "False"){
                        Boton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Activando...'
                    } else if (Dato.textContent.trim() === "True"){
                        Boton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Desactivando...'
                    }
                    e.preventDefault()
                    Boton.disabled = true;
                    const response = await fetch(`${API_BASE}/account/mfa`, {method: "PUT", headers:{"Authorization": `Bearer ${Token_JWT}`}});
                    const result = await response.json()
                    if (response.status === 200){
                        const Dato = document.getElementById("Mensaje_Mfa");
                        if (Dato.textContent.trim() === "False"){
                            sessionStorage.setItem('MFA1', "1");
                            location.reload();   
                        } else if (Dato.textContent.trim() === "True"){
                            sessionStorage.setItem('MFA2', "1");
                            location.reload();   
                        }
                    }
                    else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    }        
                    else if(response.status === 400){
                        window.scrollTo(0, 0);
                        Boton.textContent = result.Error;
                        Boton.innerHTML = Ant
                    }      
                    else if(response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    }                      
                })
            }
            if (document.getElementById("Estadisticas")){
                fetch(`${API_BASE}/case/estadisticas`, {method: "GET", headers:{"Authorization": `Bearer ${Token_JWT}`}})
                .then(respuesta =>{
                    if (respuesta.status === 401){
                        localStorage.removeItem("Token_JWT");
                        localStorage.removeItem("User_Data"); 
                        localStorage.removeItem("Auth_Token");
                        sessionStorage.removeItem("Auth_Token");
                        Swal.fire({
                            icon: 'warning',
                            title: 'Sesión expirada',
                            text: 'Debes iniciar sesión nuevamente',
                            timer: 2000,
                            showConfirmButton: false,
                            toast: true,
                            position: 'top-end',
                            background: '#1e1e2f',
                            color: '#ffffff',
                            iconColor: '#f1c40f',
                            width: '400px',
                            padding: '1.2rem',
                            customClass: {
                                popup: 'shadow-lg rounded-3'
                            }
                        });              
                        setTimeout(() => {
                            window.location.href = "/login";
                        }, 2000);
                        throw new Error("No autorizado");               
                    } else if (respuesta.status === 403) {
                        cargarPagina("/dashboard/unauthorized");
                    } else {
                        return respuesta.json();                    
                    }              
                })
                .then(Estadisticas => {
                    const Modo = document.body.classList.contains("Modo_Oscuro");
                    if (Modo) {
                        Color_Cuadricula = "rgba(255,255,255,0.07)"
                        Color_Marcas = "#999"
                        Paleta = [
                            "#378ADD",
                            "#E24B4A",
                            "#1D9E75",
                            "#F28E2B",
                            "#534AB7",
                            "#888780",
                            "#7A9E3A",
                            "#00A6A6",
                            "#BA7517",
                            "#C45D9A",
                            "#8C564B",
                            "#bd9801"
                        ];                        
                    } else {
                        Color_Cuadricula = "rgba(0,0,0,0.06)"
                        Color_Marcas = "#667"
                        Paleta = [
                            "#5BA8F5",
                            "#F07070",
                            "#2DC08A",
                            "#F5A14A",
                            "#7C6FE0",
                            "#A8A89A",
                            "#93B84A",
                            "#22C7C7",
                            "#E8A020",
                            "#D97AB5",
                            "#A8735F",
                            "#F0C93D"   
                        ];                          
                    }
                    function Crear_Leyenda(id, labels, valores, colores){
                        const Contenedor = document.getElementById(id);
                        let Total = 0;
                        for (let i = 0; i < valores.length; i++) {
                            Total = Total + valores[i];
                        };
                        labels.forEach((label, i) => {
                            const Item = document.createElement("span");
                            Item.className = "fsr-15 color_blanco2 d-flex align-items-center gap-1";

                            const Cuadro = document.createElement("span");
                            Cuadro.style.width = "9px";
                            Cuadro.style.height = "9px";
                            Cuadro.style.borderRadius = "2px";
                            Cuadro.style.display = "inline-block";                            
                            Cuadro.style.background = colores[i];

                            const Texto = document.createElement("span");
                            const Porcentaje = Math.round((valores[i] * 100) / Total);
                            if (label === "En espera del usuario"){
                                label = "En espera";
                            } else if (label === "Escalado a supervisor"){
                                label = "Escalado";
                            } else if (label === "En espera del asesor"){
                                label = "Espera asesor";
                            } else if (label === "Tomando desicion"){
                                label = "Desicion";
                            }
                            Texto.textContent = `${label}: ${Porcentaje}%`;

                            Item.appendChild(Cuadro);
                            Item.appendChild(Texto);
                            Contenedor.appendChild(Item);
                        })
                    }
                    const Opciones_Dona = {
                        responsive: true,
                        maintainAspectRatio: false,
                        cutout: "62%",
                        plugins: { 
                            legend: { display: false } 
                        }
                    };
                    const Opciones_Bar = {
                        responsive: true,
                        maintainAspectRatio: false,                        
                        plugins: { 
                            legend: { display: false } 
                        },
                        scales: {
                            x: {
                                grid: { color: Color_Cuadricula }, 
                                ticks: { 
                                    color: Color_Marcas, 
                                    font: { size: 11 } 
                                } 
                            },
                            y: { 
                                grid: { color: Color_Cuadricula }, 
                                ticks: { 
                                    color: Color_Marcas, 
                                    stepSize: 1 
                                }, 
                                beginAtZero: true 
                            }                            
                        }                       
                    }
                    const Opciones_Linea = {
                        responsive: true,
                        maintainAspectRatio: false,                        
                        plugins: { 
                            legend: { display: false } 
                        },
                        scales: {
                            x: {
                                offset: false,
                                grid: { color: Color_Cuadricula }, 
                                ticks: { 
                                    color: Color_Marcas, 
                                    font: { size: 14 } 
                                } 
                            },
                            y: { 
                                grid: { color: Color_Cuadricula }, 
                                ticks: { 
                                    color: Color_Marcas, 
                                    stepSize: 1,
                                    font: { size: 14 } 
                                }, 
                                beginAtZero: true 
                            }                            
                        }                       
                    }                    
                    if (document.getElementById("Grafica_Estados")){
                        Crear_Leyenda("Leyenda_Estado", Object.keys(Estadisticas.Estados), Object.values(Estadisticas.Estados), Paleta);
                        new Chart(document.getElementById("Grafica_Estados"),{
                            type: "doughnut",
                            data: {
                                labels: Object.keys(Estadisticas.Estados),
                                datasets: [{
                                    data: Object.values(Estadisticas.Estados),
                                    backgroundColor: Paleta,
                                    borderWidth: 0,
                                    hoverOffset: 5
                                }]                       
                            },
                            options: Opciones_Dona
                        })
                    }
                    if (document.getElementById("Grafica_Incidente")){
                        Crear_Leyenda("Leyenda_Incidente", Object.keys(Estadisticas.Incidentes), Object.values(Estadisticas.Incidentes), Paleta);
                        new Chart(document.getElementById("Grafica_Incidente"),{
                            type: 'doughnut',
                            data: {
                                labels: Object.keys(Estadisticas.Incidentes),
                                datasets: [{
                                    data: Object.values(Estadisticas.Incidentes),
                                    backgroundColor: Paleta,
                                    borderWidth: 0,
                                    hoverOffset: 5
                                }]
                            },
                            options: Opciones_Dona
                        })
                    }
                    if (document.getElementById("Grafica_Prioridad")){
                        Crear_Leyenda("Leyenda_Prioridad", Object.keys(Estadisticas.Prioridades), Object.values(Estadisticas.Prioridades), Paleta);
                        new Chart(document.getElementById("Grafica_Prioridad"),{
                            type: 'bar',
                            data: {
                                labels: Object.keys(Estadisticas.Prioridades),
                                datasets:[{
                                    data: Object.values(Estadisticas.Prioridades),
                                    backgroundColor: Paleta,
                                    borderWidth: 0,
                                    hoverOffset: 5
                                }]
                            },
                            options: Opciones_Bar
                        })
                    }
                    if (document.getElementById("Grafica_Usuario")){
                        Crear_Leyenda("Leyenda_Usuario", Object.keys(Estadisticas.Usuarios), Object.values(Estadisticas.Usuarios), Paleta)
                        new Chart(document.getElementById("Grafica_Usuario"), {
                            type: 'bar',
                            data:{
                                labels: Object.keys(Estadisticas.Usuarios),
                                datasets:[{
                                    data: Object.values(Estadisticas.Usuarios),
                                    backgroundColor: Paleta,
                                    borderWidth: 0,
                                    hoverOffset: 5
                                }]
                            },
                            options: Opciones_Bar
                        })
                    }
                    if (document.getElementById("Grafica_Tendencia")){
                        const Meses = Object.keys(Estadisticas.Tendencia_Final);
                        new Chart(document.getElementById("Grafica_Tendencia"),{
                            type: 'line',
                            data: {
                                labels: Meses,
                                datasets:[
                                    {
                                        label: "Creados",
                                        data: Meses.map(Mes => Estadisticas.Tendencia_Final[Mes].Creados),
                                        backgroundColor: "rgba(83,74,183,0.1)",
                                        borderColor: "#534AB7",
                                        pointBackgroundColor: "#534AB7",
                                        pointRadius: 4,
                                        fill: true,
                                        tension: 0.4,
                                        borderDash: []
                                    },
                                    {
                                        label: "Resueltos",
                                        data: Meses.map(Mes => Estadisticas.Tendencia_Final[Mes].Resueltos),
                                        backgroundColor: "rgba(83,74,183,0.1)",
                                        borderColor: "#1d9e75",
                                        pointBackgroundColor: "#1d9e75",
                                        fill: true,
                                        pointRadius: 4,
                                        tension: 0.4,
                                        borderDash: [5, 3]                                        
                                    }
                                ]
                            },
                            options: Opciones_Linea
                        })
                    }
                })
            }
            if (document.getElementById("Card_Estadistica_Admin")){
                const Card_Estadistica = document.getElementById("Card_Estadistica_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "estadisticas_ver")){
                    Card_Estadistica.classList.remove("d-none");
                    Card_Estadistica.classList.add("d-flex");                    
                }                       
            }        
            if (document.getElementById("Nav_Estadisticas")){
                const Nav_Estadistica = document.getElementById("Nav_Estadisticas");
                if (User.Permisos.some(Perm => Perm.Nombre === "estadisticas_ver")){
                    Nav_Estadistica.classList.remove("d-none");
                    Nav_Estadistica.classList.add("d-flex");                
                }                         
            }    
            if (document.getElementById("Estadisticas")){
                const URL = window.location.pathname;
                if (!User.Permisos.some(Perm => Perm.Nombre === "estadisticas_ver")){
                    if (URL.includes("/estadisticas")){
                        cargarPagina("/dashboard/inicio");
                    }
                }
            }           
            if (document.getElementById("Cont_Cuenta")) {
                const rol = document.getElementById("Rol_Cuenta");
                const estado = document.getElementById("Estado_Cuenta");
                const texto_rol = rol.textContent.trim()
                const texto_estado = estado.textContent.trim()
                if (texto_rol === "Administrador"){
                    rol.classList.add("badge-administrador")
                } else if (texto_rol === "Lider"){
                    rol.classList.add("badge-lider")
                } else if (texto_rol === "Analista"){
                    rol.classList.add("badge-analista")
                } else if (texto_rol === "Auxiliar"){
                    rol.classList.add("badge-auxiliar")
                } else if (texto_rol === "Revisor"){
                    rol.classList.add("badge-revisor")
                } else if (texto_rol === "Usuario"){
                    rol.classList.add("badge-usuario")
                }
                if (texto_estado === "Activo"){
                    estado.classList.add("badge-activo")
                } else if (texto_estado === "Inactivo"){
                    estado.classList.add("badge-inactivo")
                } else if (texto_estado === "Suspendido"){
                    estado.classList.add("badge-suspendido")
                } else if (texto_estado === "Bloqueado"){
                    estado.classList.add("badge-bloqueado")
                } else if (texto_estado === "Eliminado"){
                    estado.classList.add("badge-eliminado")
                }
            }
            if (document.getElementById("Cont_Cuenta")){
                const Botones = document.querySelectorAll(".Boton_Cuenta_Seccion");
                const Secciones = document.querySelectorAll(".Seccion_Cuenta");
                const List = document.querySelectorAll(".List_Cuenta");
                Botones.forEach(Boton =>{
                    Boton.addEventListener("click", () =>{
                        const Target = Boton.getAttribute("data-target");
                        
                        List.forEach(Boton =>{
                            Boton.classList.remove("background_active")
                            Boton.classList.remove("background_active2")
                        });
                        if (Boton.textContent.trim() === "Eliminacion"){
                            document.getElementById(`list_${Target}`).classList.add("background_active2")
                        } else {
                            document.getElementById(`list_${Target}`).classList.add("background_active")
                        }
                        
                        Secciones.forEach(Seccion =>{
                            Seccion.classList.remove("d-flex")
                            Seccion.classList.add("d-none")
                        })
                        document.getElementById(`seccion_${Target}`).classList.add("d-flex")
                        document.getElementById(`seccion_${Target}`).classList.remove("d-none")
                    });
                });
            }
            if (document.getElementById("seccion_1")){
                const Campos1 = document.querySelectorAll('#seccion_1 input, #seccion_1 select');
                const Boton1 = document.getElementById("seccion_1_boton");
                const Data1 = Object.fromEntries(Array.from(Campos1).map(Campo => [Campo.name, Campo.value]));
                const BotonE1 = document.getElementById("seccion_1_eliminar");
                Validar_Campos(Campos1, Data1, Boton1)
                Campos1.forEach(Campo =>{
                    Campo.addEventListener("input", () => Validar_Campos(Campos1, Data1, Boton1))
                });
                BotonE1.addEventListener("click", () =>{
                    Campos1.forEach(Campo =>{
                        Campo.value = Data1[Campo.name]
                    })
                    Validar_Campos(Campos1, Data1, Boton1)
                });
                Boton1.addEventListener("click", async function(e){
                    if (!Array.from(Campos1).every(Campo => Campo.checkValidity() || Campo.reportValidity())) return;
                    Boton1.disabled = true;
                    BotonE1.disabled = true;
                    const Boton_Antiguo = Boton1.innerHTML;
                    Boton1.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Guardando...'
                    const Data1_Envio = Object.fromEntries(Array.from(Campos1).map(Campo => [Campo.name, Campo.value]));
                    const response = await fetch(`${API_BASE}/account/update`, {method: "PUT", headers:{"Content-Type":"application/json", "Authorization":`Bearer ${Token_JWT}`}, body: JSON.stringify(Data1_Envio)});
                    const result = await response.json()   
                    
                    if(response.status === 200){
                        sessionStorage.setItem("Personal_Actualizado", User.User_ID)
                        location.reload()             
                    } else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    } else if(response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    } else if (response.status === 400){
                        const Mensaje = document.getElementById("Error_Generico");
                        Mensaje.classList.add("Message_Error")
                        Mensaje.classList.add("d-inline-flex")
                        Mensaje.classList.remove("d-none")
                        Mensaje.textContent = result.Error

                        Boton1.disabled = false;
                        Boton1.innerHTML = Boton_Antiguo
                    }
                });
            }
            if (document.getElementById("seccion_2")){
                const Campos2 = document.querySelectorAll('#Barrio_Input, #Localidad_Input, #Ciudad_Input, #Departamento_Input');
                const Boton2 = document.getElementById("seccion_2_boton");
                const Data2 = Object.fromEntries(Array.from(Campos2).map(Campo => [Campo.name, Campo.value]));
                const BotonE2 = document.getElementById("seccion_2_eliminar");
                Validar_Campos(Campos2, Data2, Boton2)
                Campos2.forEach(Campo =>{
                    Campo.addEventListener("input", () => Validar_Campos(Campos2, Data2, Boton2))
                })
                BotonE2.addEventListener("click", () =>{
                    Campos2.forEach(Campo =>{
                        Campo.value = Data2[Campo.name]
                    })
                    Validar_Campos(Campos2, Data2, Boton2)
                })
                Boton2.addEventListener("click", async function(e){
                    if (!Array.from(Campos2).every(Campo => Campo.checkValidity() || Campo.reportValidity())) return;                    
                    Boton2.disabled = true;
                    BotonE2.disabled = true;
                    Boton2.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Guardando...'
                    const Data2_Envio = Object.fromEntries(Array.from(Campos2).map(Campo => [Campo.name, Campo.value]));
                    const response = await fetch(`${API_BASE}/account/update/place`, {method: "PUT", headers:{"Content-Type":"application/json", "Authorization":`Bearer ${Token_JWT}`}, body: JSON.stringify(Data2_Envio)});
                    if(response.status === 200){
                        sessionStorage.setItem("Personal_Actualizado", User.User_ID)
                        location.reload()             
                    } else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    } else if(response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    }                    
                })
            }
            if (document.getElementById("seccion_3")){
                const Campos3 = document.querySelectorAll("#seccion_3 input");
                const Boton3 = document.getElementById("seccion_3_boton");
                const Boton_Ant3 = Boton3.innerHTML;
                const BotonE3 = document.getElementById("seccion_3_eliminar");
                const Data3 = Object.fromEntries(Array.from(Campos3).map(Campo => [Campo.name, Campo.value]));                
                Boton3.disabled = true;
                Campos3.forEach(Campo => {
                    Campo.addEventListener("input", () => {
                        Boton3.disabled = Array.from(Campos3).some(Campo => Campo.value.trim() === "");
                    });
                });                
                BotonE3.addEventListener("click", () =>{
                    Campos3.forEach(Campo =>{
                        Campo.value = Data3[Campo.name]
                    })
                    Validar_Campos(Campos3, Data3, Boton3)
                })
                Boton3.addEventListener("click", async function(e) {
                    if (!Array.from(Campos3).every(Campo => Campo.checkValidity() || Campo.reportValidity())) return;
                    const Mensaje = document.getElementById("Error_Generico3");
                    Mensaje.classList.remove("d-inline-flex");
                    Mensaje.classList.remove("Message_Error");
                    Mensaje.classList.add("d-none");                    
                    Boton3.disabled = true;
                    BotonE3.disabled = true;
                    Boton3.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Guardando...'
                    const Data3_Envio = Object.fromEntries(Array.from(Campos3).map(Campo => [Campo.name, Campo.value]));
                    const Contraseña_Nueva1 = document.getElementById("Contraseña_Nueva");
                    const Contraseña_Nueva2 = document.getElementById("Contraseña_Nueva2");       
                    if (Contraseña_Nueva1.value !== Contraseña_Nueva2.value){
                        Boton3.disabled = false;
                        Boton3.innerHTML = Boton_Ant3;
                        BotonE3.disabled = false;
                        Mensaje.classList.add("d-inline-flex");
                        Mensaje.classList.add("Message_Error");
                        Mensaje.classList.remove("d-none");
                        Mensaje.textContent = "Las contraseñas no coinciden"
                        return;
                    }
                    
                    const response = await fetch(`${API_BASE}/account/update/password`, {method: "PUT", headers:{"Content-Type":"application/json", "Authorization":`Bearer ${Token_JWT}`}, body: JSON.stringify(Data3_Envio)});
                    const result = await response.json()   

                    if(response.status === 200){
                        sessionStorage.setItem("Personal_Actualizado", User.User_ID)
                        location.reload()             
                    } else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    } else if(response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    } else if (response.status === 400){
                        Mensaje.classList.add("Message_Error")
                        Mensaje.classList.add("d-inline-flex")
                        Mensaje.classList.remove("d-none")
                        Mensaje.textContent = result.Error

                        Boton3.disabled = false;
                        Boton3.innerHTML = Boton_Ant3;
                        BotonE3.disabled = false;
                    }                    
                })
            }
            if (document.getElementById("seccion_4")){
                const Boton4 = document.getElementById("Boton_Subir_Imagen");
                const BotonE4 = document.getElementById("Boton_Eliminar_Imagen");
                const Input_Image = document.getElementById("image_input");

                const Modal_Cropper = document.getElementById("Modal_Cropper");
                const Imagen_Cropper = document.getElementById("Imagen_Cropper");   
                const Modal_Boton_Cancelar = document.getElementById("Btn_Cancelar_Crop");
                const Modal_Boton_Confirmar = document.getElementById("Btn_Confirmar_Crop");
                let cropper; 

                async function SubirImagen(Imagen) {
                    const Mensaje = document.getElementById("Error_Generico4");
                    const Boton4_Ant = Boton4.innerHTML;

                    Mensaje.classList.remove("Message_Error");
                    Mensaje.classList.remove("d-inline-flex");
                    Mensaje.classList.add("d-none");

                    Boton4.disabled = true;
                    BotonE4.disabled = true;
                    Boton4.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Subiendo...';

                    const formData = new FormData();
                    formData.append("imagen_usuario", Imagen);

                    const response = await fetch(`${API_BASE}/account/update/image`, {method: "PUT", headers:{"Authorization":`Bearer ${Token_JWT}`}, body: formData});
                    const result = await response.json();
                    
                    if (response.status === 200){
                        sessionStorage.setItem("Personal_Actualizado", User.User_ID);
                        User.Nombre_Imagen = result.Nombre_Nuevo;
                        localStorage.setItem("User_Data", JSON.stringify(User));
                        location.reload();
                    } else if (response.status === 429){
                        window.location.href = "/rate-limit";
                    } else if (response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    } else if (response.status === 400){
                        Mensaje.classList.add("Message_Error");
                        Mensaje.classList.add("d-inline-flex");
                        Mensaje.classList.remove("d-none");
                        Mensaje.textContent = result.Error;
                        BotonE4.disabled = false;
                        Boton4.disabled = false;
                        Boton4.innerHTML = Boton4_Ant;
                        Input_Image.value = "";
                    }
                }                
                Input_Image.addEventListener("change", function() {
                    const Imagen = this.files[0];
                    if (!Imagen) return;
                    const Extension = Imagen.name.split(".").pop().toLowerCase();
                    if (!["jpg", "jpeg", "png"].includes(Extension)) {
                        Input_Image.value = "";
                        return;
                    }                    
                    Imagen_Cropper.src = URL.createObjectURL(Imagen);
                    Modal_Cropper.classList.replace("d-none", "d-flex");
                    Imagen_Cropper.onload = () => {
                        if (cropper) cropper.destroy();
                        cropper = new Cropper(Imagen_Cropper, { aspectRatio: 1, viewMode: 1 });
                    };
                });                
                Modal_Boton_Cancelar.addEventListener("click", function() {
                    Modal_Cropper.classList.replace("d-flex", "d-none");
                    Input_Image.value = "";
                    if (cropper) cropper.destroy();
                })
                Modal_Boton_Confirmar.addEventListener("click", function() {
                    cropper.getCroppedCanvas({ width: 300, height: 300 }).toBlob((blob) => {
                        const Archivo = new File([blob], "imagen.jpg", { type: "image/jpeg" });
                        Modal_Cropper.classList.replace("d-flex", "d-none");
                        SubirImagen(Archivo);
                    }, "image/jpeg");
                })
                BotonE4.addEventListener("click", async function(e) {
                    const BotonE4_Ant = BotonE4.innerHTML
                    BotonE4.disabled = true
                    Boton4.disabled = true
                    BotonE4.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Eliminando...'
                    const response = await fetch(`${API_BASE}/account/delete/image`, {method: "PUT", headers:{"Content-Type":"application/json", "Authorization":`Bearer ${Token_JWT}`}});
                    const result = await response.json()   
                    if(response.status === 200){
                        sessionStorage.setItem("Personal_Actualizado", User.User_ID)
                        location.reload()             
                    } else if(response.status === 429){
                        window.location.href = "/rate-limit"
                    } else if(response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    } else if (response.status === 400){
                        const Mensaje = document.getElementById("Error_Generico4")
                        Mensaje.classList.add("Message_Error")
                        Mensaje.classList.add("d-inline-flex")
                        Mensaje.classList.remove("d-none")
                        Mensaje.textContent = result.Error

                        BotonE4.disabled = false;
                        Boton4.disabled = false;
                        BotonE4.innerHTML = BotonE4_Ant;
                    }                                       
                })                
            }
            if (document.getElementById("seccion_6")){
                const Devices_Buton = document.getElementById("Delete_Devices");
                const Account_Buton = document.getElementById("Delete_Account");
                Devices_Buton.addEventListener("click", async function (e) {
                    if (!confirm("¿Seguro que quieres cerrar todos los dispositivos?")) return;
                    Devices_Buton.disabled = true;
                    const Devices_Buton_Ant = Devices_Buton.innerHTML
                    Devices_Buton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Eliminando...'

                    const response = await fetch(`${API_BASE}/account/delete/devices`, {method: "PUT", headers:{"Authorization":`Bearer ${Token_JWT}`}});
                    const result = await response.json();
                    
                    if (response.status === 200){
                        localStorage.removeItem("Auth_Token")
                        localStorage.removeItem("Device_Token")
                        sessionStorage.removeItem("Auth_Token")
                        window.location.href = "/login";                    
                        sessionStorage.setItem("Personal_Actualizado", User.User_ID);
                        location.reload();
                    } else if (response.status === 429){
                        window.location.href = "/rate-limit";
                    } else if (response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    } else if (response.status === 400){
                        Devices_Buton.disabled = false;
                        Devices_Buton.innerHTML = Devices_Buton_Ant;
                    }                    
                })
                Account_Buton.addEventListener("click", async function (e) {
                    if (!confirm("¿Seguro que quieres eliminar tu cuenta? Esta acción no se puede deshacer.")) return;
                    Account_Buton.disabled = true;
                    const Account_Buton_Ant = Account_Buton.innerHTML
                    Account_Buton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Eliminando...'

                    const response = await fetch(`${API_BASE}/account/delete/account`, {method: "PUT", headers:{"Authorization":`Bearer ${Token_JWT}`}});
                    const result = await response.json();
                    
                    if (response.status === 200){
                        localStorage.removeItem("Auth_Token")
                        localStorage.removeItem("Device_Token")
                        sessionStorage.removeItem("Auth_Token")
                        window.location.href = "/login";                                       
                        sessionStorage.setItem("Personal_Actualizado", User.User_ID);
                        location.reload();
                    } else if (response.status === 429){
                        window.location.href = "/rate-limit";
                    } else if (response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    } else if (response.status === 400){
                        Account_Buton.disabled = false;
                        Account_Buton.innerHTML = Account_Buton_Ant;
                    }                    
                })
            }
            if (document.getElementById("Excel_Button")){
                const Boton = document.getElementById("Excel_Button");
                if (User.Permisos.some(Perm => Perm.Nombre === "exportar_excel")){
                    Boton.classList.remove("d-none");
                    Boton.classList.add("d-flex")
                }             
                Boton.addEventListener("click", async function(e) {
                    Boton.disabled = true
                    Boton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>Descargando...'

                    const response = await fetch(`${API_BASE}/case/excel`, {method: "GET", headers:{"Authorization": `Bearer ${Token_JWT}`}});
                    
                    if (response.status === 200){
                        const Blob = await response.blob();
                        const Url = window.URL.createObjectURL(Blob);
                        const Disposition = response.headers.get("Content-Disposition");
                        let filename = "Reporte_Casos.xlsx";
                        if (Disposition && Disposition.includes("filename=")){
                            filename = Disposition.split("filename=")[1].replace(/"/g, "")
                        }
                        const a = document.createElement("a");
                        a.href = Url;
                        a.download = filename;
                        document.body.appendChild(a);
                        a.click();
                        a.remove();
                        window.URL.revokeObjectURL(Url)
                        sessionStorage.setItem("Excel", User.User_ID)
                        location.reload()
                    } else if (response.status === 429){
                        window.location.href = "/rate-limit"
                    } else if(response.status === 403){
                        cargarPagina("/dashboard/unauthorized");
                    }
                })
            }
            if (document.getElementById("Form_Ayuda_For")){
                const Botones = document.querySelectorAll(".Boton_Ayuda_Eliminar");
                Botones.forEach(Boton => {
                    Boton.addEventListener("click", async function (e) {
                        Boton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#dd9898" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>'
                        const btn_id = Boton.dataset.id
                        const response = await fetch(`${API_BASE}/forms/ayuda/delete/${btn_id}`, {method: "DELETE"});
                        if(response.status === 200){
                            sessionStorage.setItem('form_eliminado', btn_id);                        
                            location.reload();
                        }
                    })
                });
            }
            if (document.getElementById("Form_Calificanos_For")){
                const Botones = document.querySelectorAll(".Boton_Calificanos_Eliminar");
                Botones.forEach(Boton => {
                    Boton.addEventListener("click", async function (e) {
                        Boton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#dd9898" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>'
                        const btn_id = Boton.dataset.id
                        const response = await fetch(`${API_BASE}/forms/calificanos/delete/${btn_id}`, {method: "DELETE"});
                        if(response.status === 200){
                            sessionStorage.setItem('form_eliminado', btn_id);                        
                            location.reload();
                        }
                    })
                });
            } 
            if (document.getElementById("Form_Contactanos_For")){
                const Botones = document.querySelectorAll(".Boton_Contactanos_Eliminar");
                Botones.forEach(Boton => {
                    Boton.addEventListener("click", async function (e) {
                        Boton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><rect width="24" height="24" fill="none"/><path fill="none" stroke="#dd9898" stroke-linecap="round" stroke-linejoin="round" stroke-width="4" d="M12 3c4.97 0 9 4.03 9 9"><animateTransform attributeName="transform" dur="1.5s" repeatCount="indefinite" type="rotate" values="0 12 12;360 12 12"/></path></svg>'
                        const btn_id = Boton.dataset.id
                        const response = await fetch(`${API_BASE}/forms/contactanos/delete/${btn_id}`, {method: "DELETE"});
                        if(response.status === 200){
                            sessionStorage.setItem('form_eliminado', btn_id);                        
                            location.reload();
                        }
                    })
                });
            } 
            if (document.getElementById("Nav_Forms_Admin")){
                const Nav = document.getElementById("Nav_Forms_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver")){
                    Nav.classList.remove("d-none");
                    Nav.classList.add("d-flex");                
                }                        
            }
            if (document.getElementById("Card_Forms_Admin")){
                const Card = document.getElementById("Card_Forms_Admin");
                if (User.Permisos.some(Perm => Perm.Nombre === "caso_ver")){
                    Card.classList.remove("d-none");
                    Card.classList.add("d-flex");                    
                }               
            }                                   
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

    cargarPagina(path + window.location.search);
});
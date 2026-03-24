const API_BASE = 'https://p8kjdpww-5000.use2.devtunnels.ms';

document.addEventListener("DOMContentLoaded", () => {
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
    
    
    const Contenido = document.getElementById("contenido");
    const contenidoOriginal = Contenido.innerHTML;

    function cargarPagina(url) {
        Contenido.innerHTML = contenidoOriginal;       
        fetch(url, {
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(res => res.text())
        .then(html => {
            Contenido.innerHTML = html;
            history.pushState(null, "", url);
            const User = JSON.parse(localStorage.getItem("User_Data"));
            if (document.getElementById("User_Name")){
                document.getElementById("User_Name").textContent = User.User_Name;
            }            
            if (document.getElementById("User_Name2")){
                document.getElementById("User_Name2").textContent = User.User_Name;
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
                    const Nombre_Usuario = User.User_Name;
                    const GCS_URL = `https://storage.googleapis.com/gaialink/${Nombre_Usuario}.png`;
                    const DEFAULT = '/Statics/img/USER_DEFAULT.svg';   
                    
                    img2.onerror = function(){
                        if (this.dataset.fallback !== "true"){
                            this.dataset.fallback = "true";
                            this.src = DEFAULT;
                        }
                    };      
                    
                    img2.src = `${GCS_URL}?_=${Date.now()}`;                    
                }
                document.querySelectorAll(".imagen_usuario").forEach(img =>{
                    const Nombre_Usuario = User.User_Name;
                    const GCS_URL = `https://storage.googleapis.com/gaialink/${Nombre_Usuario}.png`;
                    const DEFAULT = '/Statics/img/USER_DEFAULT.svg';

                    img.onerror = function(){
                        if (this.dataset.fallback !== "true"){
                            this.dataset.fallback = "true";
                            this.src = DEFAULT;
                        }
                    };      
                    
                    img.src = `${GCS_URL}?_=${Date.now()}`;
                });
                document.querySelectorAll("[id^='Imagen_Usuario_Comentario_']").forEach(Img_Com => {
                    const id = Img_Com.id.split("_").pop();
                    const Nombre_Usuario = document.getElementById(`Obtener_Usuario_Comentario_${id}`).textContent.trim();
                    const GCS_URL = `https://storage.googleapis.com/gaialink/${Nombre_Usuario}.png`;
                    const DEFAULT = '/Statics/img/USER_DEFAULT.svg';

                    Img_Com.onerror = function(){
                        if (this.dataset.fallback !== "true"){
                            this.dataset.fallback = "true";
                            this.src = DEFAULT;
                        }
                    };     
                    
                    Img_Com.src = `${GCS_URL}?_=${Date.now()}`;
                });
            }
            if (document.getElementById("Agregar_Trabajo")){
                Boton = document.getElementById("Agregar_Trabajo")
                Mensaje_Boton = document.getElementById("Agregar_Trabajo_Mensaje")
                Imagen_Boton = document.getElementById("Agregar_Trabajo_Imagen")
                Card = document.getElementById("Crear_Relacion")
                Boton.addEventListener("click", () => {
                    if (Card.classList.contains("d-none")) {
                        Card.classList.remove("d-none");
                        Mensaje_Boton.textContent = "Eliminar trabajo";
                        Imagen_Boton.src = "/Statics/img/Minus.svg";
                        document.getElementById("Relacion_Tipo").required = true;
                        document.getElementById("Relacion_Radicado").required = true;
                    }else if (!Card.classList.contains("d-none")){
                        document.getElementById("Relacion_Tipo").selectedIndex = 0;
                        document.getElementById("Relacion_Radicado").selectedIndex = 0;
                        document.getElementById("Relacion_Tipo").required = false;
                        document.getElementById("Relacion_Radicado").required = false;                        
                        Mensaje_Boton.textContent = "Añadir trabajo";
                        Imagen_Boton.src = "/Statics/img/Plus.svg";
                        Card.classList.add("d-none");
                    }
                });
            }
            if (document.getElementById("Caso_Contenedor")) {
                const Contenedor = document.getElementById("Caso_Contenedor");
                const Boton = document.getElementById("Caso_Boton_Guardar");
                const Boton2 = document.getElementById("Caso_Boton_Recarga");
                const Imagen = document.getElementById("Caso_Boton_Guardar_Img");
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
                    Boton = document.getElementById("Caso_Boton_Guardar");
                    Boton_Mensaje = document.getElementById("Caso_Boton_Guardar_Msg");
                    Boton.disabled = true;
                    Id = document.getElementById("Obtener_Caso_Id").textContent.trim();

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

                    const response = await fetch(`${API_BASE}/api/case/update/${Id}`, {method: "PUT", headers:{"Content-Type":"application/json"},body: JSON.stringify(data)});
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
                });
            }   
            if (document.getElementById("Caso_Contenedor2")){
                document.getElementById("Caso_Contenedor2").addEventListener("submit", async function(e){
                    e.preventDefault();
                    Boton = document.getElementById("CasoNuevo_Boton_Guardar");
                    Boton_Mensaje = document.getElementById("CasoNuevo_Boton_Guardar_Msg");
                    Boton.disabled = true;

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
                    
                    const response = await fetch(`${API_BASE}/api/case/create`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(data)});
                    const result = await response.json()
                    
                    if(response.status === 200){
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
                });
            }                    
            if (document.getElementById("Caso_Contenedor")){
                document.querySelectorAll("[id^='Caso_Boton_Eliminar_']").forEach(span => {
                    const caseId = span.dataset.caseId;
                    span.addEventListener("click", async (e) =>{
                        span.disabled = true;
                        const response = await fetch(`${API_BASE}/api/case/delete/${caseId}/${User.User_ID}`, {method: "PUT"});
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
                    });
                });
                document.querySelectorAll("[id^='Boton_Relacion_']").forEach(el =>{
                    
                    el.addEventListener("click", async (e) =>{
                        el.disabled = true;
                        Rad_Padre = el.dataset.radPadre;
                        Rad_Hijo = el.dataset.radHijo;
                        Tipo_Relacion = el.dataset.radTipo;                        
                        const response = await fetch(`${API_BASE}/api/case/delete/relation/${Rad_Padre}/${Rad_Hijo}/${Tipo_Relacion}/${User.User_ID}`, {method: "DELETE"});
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
                    cargarPagina("/dashboard/casos/search?" + params.toString());
                });
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
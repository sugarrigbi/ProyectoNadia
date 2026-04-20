const API_BASE = 'https://p8kjdpww-5000.use2.devtunnels.ms';

if (document.getElementById("Formulario_Ayuda")){
    document.getElementById("Formulario_Ayuda").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Ayuda_Boton");        
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Ayuda_Mensaje");
        Boton.disabled = true;
        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        const response = await fetch(`${API_BASE}/api/forms/ayuda/create`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(data)});

        if(response.status === 201){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
            Boton.disabled = true;

            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }        
        else if(response.status === 400){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");
            Boton.disabled = false;
            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Error");

            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
    });
}
if (document.getElementById("Formulario_Calificanos")){
    document.getElementById("Formulario_Calificanos").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Calificanos_Boton");        
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Calificanos_Mensaje");
        Boton.disabled = true;
        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        const response = await fetch(`${API_BASE}/api/forms/calificanos/create`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(data)});

        if(response.status === 201){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
            Boton.disabled = true;
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }        
        else if(response.status === 400){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");
            Boton.disabled = false;
            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Error");

            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
    });
}
if (document.getElementById("Formulario_Contactanos")){
    document.getElementById("Formulario_Contactanos").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Contactanos_Boton");
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Contactanos_Mensaje");
        Boton.disabled = true;
        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        const response = await fetch(`${API_BASE}/api/forms/contactanos/create`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(data)});

        if(response.status === 201){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
            Boton.disabled = true;
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }
        else if(response.status === 400){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Error");
            Boton.disabled = false;
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
    });
}
if (document.getElementById("Formulario_Registrar")){
    document.getElementById("Formulario_Registrar").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Registrar_Boton");        
        document.querySelectorAll("[id^='Error_']").forEach(el => {
            el.classList.add("d-none");
        });     
        if(!this.checkValidity()){
            const input = this.querySelector(":invalid")
            if (input.validity.valueMissing) {
                if (input.name === "Recordar"){
                    Mensaje_Text = "Acepta los terminos y condiciones";
                }
                else {
                    Mensaje_Text = "Completa este campo";
                }                
            }
            else if (input.validity.typeMismatch) {
                Mensaje_Text = "Correo inválido";
            }
            else if (input.validity.patternMismatch) {
                if (input.name === "Fecha_Nacimiento" || input.name === "Documento"){
                    Mensaje_Text = "Solo se permite numeros";
                }
                else {
                    Mensaje_Text = "Solo se permite letras";
                }
            }
            else if (input.validity.tooShort) {
                Mensaje_Text = `Mínimo ${input.minLength} caracteres`;
            }
            else if (input.validity.tooLong) {
                Mensaje_Text = `Máximo ${input.maxLength} caracteres`;
            }
            else if (input.validity.rangeUnderflow) {
                Mensaje_Text = `Debe ser mayor o igual a ${input.min}`;
            }
            else if (input.validity.rangeOverflow) {
                Mensaje_Text = `Debe ser menor o igual a ${input.max}`;
            }
            else if (input.validity.stepMismatch) {
                Mensaje_Text = "Valor no válido";
            }
            else if (input.validity.badInput) {
                Mensaje_Text = "Dato inválido";
            }  
            Mensaje = document.getElementById(`Error_${input.name}`);
            Mensaje.classList.remove("d-none");
            Mensaje.classList.add("Message_Error"); 
            Mensaje.textContent = Mensaje_Text
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            return; 
        }        
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");                 
        Mensaje = document.getElementById("Formulario_Registrar_Mensaje");
        Boton.disabled = true;
        
        const Pass1 = document.getElementById("Input_Password1").value;
        const Pass2 = document.getElementById("Input_Password2").value;

        if(Pass1 !== Pass2){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.setAttribute("data-lang", "formularios.Error_Contraseña");

            CambiarIdioma(localStorage.getItem("idioma") || "es");
            Boton.disabled = false;         
            return;   
        }

        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());
        const response = await fetch(`${API_BASE}/api/registro`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(data)});
        const result = await response.json()

        if(response.status === 200){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
            window.location.href = "/registro/codigo"
            Boton.disabled = true;
            localStorage.setItem("Correo_Registro", data.Correo)
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }        
        else if(response.status === 400){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.textContent = result.Error;
            Boton.disabled = false;
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
    });
}
if (document.getElementById("Formulario_Autenticador")){
    document.getElementById("Formulario_Autenticador").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Autenticador_Boton"); 
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Autenticador_Mensaje");
        Boton.disabled = true; 

        const Inputs = document.querySelectorAll("input[type='text']");
        const codigo = Array.from(Inputs).map(input => input.value).join("");        
        
        const payload = {
            Identificador: localStorage.getItem("Identificador_Login"),
            Codigo_User: codigo
        };        

        const response = await fetch(`${API_BASE}/api/login/mfa`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(payload)});
        const result = await response.json() 
        const expiresAtStr = result.Expires_At
        const expiresAtMs = Date.parse(expiresAtStr);
        const expiresAt = Math.floor(expiresAtMs / 1000);

        if(response.status === 200){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");
            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
            Boton.disabled = true;
            localStorage.setItem("Device_Token", result.Device);
            localStorage.setItem("Token_JWT", result.Token);
            localStorage.setItem("User_Data", JSON.stringify(result.User));
            if (result.Remember_Me) {
                localStorage.setItem("Auth_Token", result.Token);
                localStorage.setItem("Auth_ExpiresAt", String(expiresAt));
            } else {
                sessionStorage.setItem("Auth_Token", result.Token);
                sessionStorage.setItem("Auth_ExpiresAt", String(expiresAt));
            }
            window.location.href = "/dashboard"
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }        
        else if(response.status === 400 || response.status === 401 || response.status === 403){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");
            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.textContent = result.Error;
            Boton.disabled = false;
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }                       
    })
}
if (document.getElementById("Formulario_Codigo")){
    document.getElementById("Formulario_Codigo").addEventListener("submit", async function(e){
        e.preventDefault(); 
        Boton = document.getElementById("Formulario_Codigo_Boton");        
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Codigo_Mensaje");
        Boton.disabled = true;

        const Inputs = document.querySelectorAll("input[type='text']");
        const codigo = Array.from(Inputs).map(input => input.value).join("");
        const correoGuardado = localStorage.getItem("Correo_Registro") || "";

        const payload = {
            Correo: correoGuardado,
            Codigo: codigo
        };

        const response = await fetch(`${API_BASE}/api/registro/codigo`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(payload)});
        const result = await response.json()        

        if(response.status === 200){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
            Boton.disabled = true;
            localStorage.removeItem("Correo_Registro");
            window.location.href = "/login"
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }        
        else if(response.status === 400){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.textContent = result.Error;
            Boton.disabled = false;
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
    });
}
if (document.getElementById("Formulario_Login")){
    document.getElementById("Formulario_Login").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Login_Boton");        
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Login_Mensaje");
        Boton.disabled = true;    

        const Info = {
            userAgent: navigator.userAgent || null,
            uaData: navigator.userAgentData ? {
                platform: navigator.userAgentData.platform || null,
                brands: navigator.userAgentData.brands || null,
                mobile: navigator.userAgentData.mobile || null
            } : null,
            screen: { width: screen.width, height: screen.height }
        };

        const payload = {
            Identificador: document.getElementById("Identificacion").value,
            Contraseña: document.getElementById("Input_Password3").value,
            Remember_Me: document.getElementById("Remember_Me").checked,
            Dispositivo: localStorage.getItem("Device_Token") || "",
            Client_Payload: Info
        }; 
        
        const response = await fetch(`${API_BASE}/api/login`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(payload)});
        const result = await response.json()

        const expiresAtStr = result.Expires_At
        const expiresAtMs = Date.parse(expiresAtStr);
        const expiresAt = Math.floor(expiresAtMs / 1000);
        
        if(result.MFA){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");
            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
            Boton.disabled = true;
            localStorage.setItem("Identificador_Login", payload.Identificador);
            window.location.href = "/login/autenticador"
        } else {
            if(response.status === 200){
                Boton.classList.remove("boton2");
                Boton.classList.add("boton5");
                Boton.classList.remove("Bg_Azul4");
                Boton.classList.add("Bg_Verde");
                Boton.setAttribute("data-lang", "formularios.Enviado");

                Mensaje.classList.remove("d-none");
                Mensaje.style.display = 'block';
                Mensaje.classList.add("Message_Success"); 
                Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");
                Boton.disabled = true;
                localStorage.setItem("Device_Token", result.Device);
                localStorage.setItem("Token_JWT", result.Token);
                localStorage.setItem("User_Data", JSON.stringify(result.User));
                if (payload.Remember_Me) {
                    localStorage.setItem("Auth_Token", result.Token);
                    localStorage.setItem("Auth_ExpiresAt", String(expiresAt));

                } else {
                    sessionStorage.setItem("Auth_Token", result.Token);
                    sessionStorage.setItem("Auth_ExpiresAt", String(expiresAt));
                }
                window.location.href = "/dashboard"
                CambiarIdioma(localStorage.getItem("idioma") || "es");
            }
            else if(response.status === 429){
                window.location.href = "/rate-limit"
            }        
            else if(response.status === 400 || response.status === 401 || response.status === 403){
                Boton.classList.remove("boton2");
                Boton.classList.add("boton6");
                Boton.classList.remove("Bg_Azul4");
                Boton.classList.add("Bg_Rojo");
                Boton.setAttribute("data-lang", "formularios.Error");

                Mensaje.classList.remove("d-none");
                Mensaje.style.display = 'block';
                Mensaje.classList.add("Message_Error"); 
                Mensaje.textContent = result.Error;
                Boton.disabled = false;
                CambiarIdioma(localStorage.getItem("idioma") || "es");
            } 
        }       
    });
}
if (document.getElementById("Formulario_Recuperar")){
    document.getElementById("Formulario_Recuperar").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Recuperar_Boton");        
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Recuperar_Mensaje");
        Boton.disabled = true;

        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());
        const response = await fetch(`${API_BASE}/api/recuperar`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(data)});
        const result = await response.json()

        if (response.status === 200) {
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");
            Boton.disabled = true;

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");

            localStorage.setItem("Identificador_Recuperar", data.Identificador)
            window.location.href = "/login/recuperar/codigo"
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }        
        else if (response.status === 400 || response.status === 401) {
            window.scrollTo(0, 0);
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");
            Boton.disabled = false;

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.textContent = result.Error;
            
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
    });
}
if (document.getElementById("Formulario_Recuperar2")){
    document.getElementById("Formulario_Recuperar2").addEventListener("submit", async function(e){
        e.preventDefault();
        Boton = document.getElementById("Formulario_Recuperar2_Boton");        
        Boton.setAttribute("data-lang", "formularios.Enviar");
        Boton.classList.remove("Bg_Rojo");
        Boton.classList.remove("boton6");        
        Boton.classList.add("Bg_Azul4");
        Boton.classList.add("boton2");          
        Mensaje = document.getElementById("Formulario_Recuperar2_Mensaje");
        Boton.disabled = true;

        const Pass1 = document.getElementById("Input_Password4").value;
        const Pass2 = document.getElementById("Input_Password5").value;

        if(Pass1 !== Pass2){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.setAttribute("data-lang", "formularios.Error_Contraseña");

            CambiarIdioma(localStorage.getItem("idioma") || "es");
            Boton.disabled = false;         
            return;   
        }        
        
        const Codigo_1 = document.getElementById("Input_1").value;
        const Codigo_2 = document.getElementById("Input_2").value;
        const Codigo_3 = document.getElementById("Input_3").value;
        const Codigo_4 = document.getElementById("Input_4").value;
        const Codigo_5 = document.getElementById("Input_5").value;
        const Codigo_6 = document.getElementById("Input_6").value;

        const Codigo = Codigo_1+Codigo_2+Codigo_3+Codigo_4+Codigo_5+Codigo_6;

        const Identificador_Guardado = localStorage.getItem("Identificador_Recuperar") || "";

        const payload = {
            Identificador: Identificador_Guardado,
            Codigo: Codigo,
            Contraseña: document.getElementById("Input_Password5").value
        };

        const response = await fetch(`${API_BASE}/api/recuperar/codigo`, {method: "POST", headers:{"Content-Type":"application/json"},body: JSON.stringify(payload)});
        const result = await response.json()        

        if(response.status === 200){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton5");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Verde");
            Boton.setAttribute("data-lang", "formularios.Enviado");
            Boton.disabled = true;

            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Success"); 
            Mensaje.setAttribute("data-lang", "formularios.Enviar_Exito");

            localStorage.removeItem("Identificador_Recuperar");
            window.location.href = "/login"
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
        else if(response.status === 429){
            window.location.href = "/rate-limit"
        }        
        else if(response.status === 400 || response.status === 401){
            Boton.classList.remove("boton2");
            Boton.classList.add("boton6");
            Boton.classList.remove("Bg_Azul4");
            Boton.classList.add("Bg_Rojo");
            Boton.setAttribute("data-lang", "formularios.Error");
            Boton.disabled = false;
            Mensaje.classList.remove("d-none");
            Mensaje.style.display = 'block';
            Mensaje.classList.add("Message_Error"); 
            Mensaje.textContent = result.Error;
            CambiarIdioma(localStorage.getItem("idioma") || "es");
        }
    });
}
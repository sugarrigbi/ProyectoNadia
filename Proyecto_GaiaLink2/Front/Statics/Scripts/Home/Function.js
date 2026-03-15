if (document.getElementById("Input_Password1")){
    Input1 = document.getElementById("Input_Password1");
    Boton1 = document.getElementById("Boton_Password1");
    Imagen1 = document.getElementById("Imagen_Password1");    
    Boton1.addEventListener("click", () => {
        if (Input1.type === "password"){
            Input1.type = "text"
            Imagen1.src = "Statics/img/Ver.svg"
        }
        else if (Input1.type === "text"){
            Input1.type = "password"
            Imagen1.src = "Statics/img/NoVer.svg"
        }    
    });
}
if (document.getElementById("Input_Password2")){
    Input2 = document.getElementById("Input_Password2");
    Boton2 = document.getElementById("Boton_Password2");
    Imagen2 = document.getElementById("Imagen_Password2");    
    Boton2.addEventListener("click", () => {
        if (Input2.type === "password"){
            Input2.type = "text"
            Imagen2.src = "Statics/img/Ver.svg"
        }
        else if (Input2.type === "text"){
            Input2.type = "password"
            Imagen2.src = "Statics/img/NoVer.svg"
        }     
    });
}
if (document.getElementById("Input_Password3")){
    Input3 = document.getElementById("Input_Password3");
    Boton3 = document.getElementById("Boton_Password3");
    Imagen3 = document.getElementById("Imagen_Password3");    
    Boton3.addEventListener("click", () => {
        if (Input3.type === "password"){
            Input3.type = "text"
            Imagen3.src = "Statics/img/Ver.svg"
        }
        else if (Input3.type === "text"){
            Input3.type = "password"
            Imagen3.src = "Statics/img/NoVer.svg"
        }     
    });
}
if (document.getElementById("Input_Container")){
    const Inputs = document.querySelectorAll("input[type='text']")

    Inputs.forEach((Input, Index) =>{
        Input.addEventListener("input", () =>{
            if (Input.value.length === 1 && Index < Inputs.length -1){
                Inputs[Index+1].focus();
            }
        });
        Input.addEventListener("keydown", (e) =>{
            if (e.key === "Backspace" && Input.value === "" && Index > 0){
                Inputs[Index-1].focus()
            }
        });
    });
}
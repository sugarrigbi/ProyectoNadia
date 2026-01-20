document.addEventListener("DOMContentLoaded", () => {
  const descripcion = document.getElementById("descripcion");
  const contador = document.getElementById("contador");

  descripcion.addEventListener("input", function (e) {
    const longitudMax = e.target.getAttribute("maxlength");
    const longitudAct = e.target.value.length;
    const porcentaje = (longitudAct / longitudMax) * 100;

    contador.innerHTML = `${longitudAct}/${longitudMax}`;

    // Resetear clases de color
    contador.classList.remove("text-success", "text-warning", "text-danger");

    if (porcentaje < 80) {
      contador.classList.add("text-success"); // verde
    } else if (porcentaje < 100) {
      contador.classList.add("text-warning"); // naranja
    } else {
      contador.classList.add("text-danger"); // rojo
    }
  });
});

function showToast(message, type = "success") {
  const toastEl = document.getElementById("toast");
  const msg = document.getElementById("toast-message");

  // Mensaje dinámico
  msg.textContent = message;

  // Colores según tipo
  toastEl.classList.remove("bg-success", "bg-danger", "bg-warning");
  if (type === "success") toastEl.classList.add("bg-success");
  else if (type === "error") toastEl.classList.add("bg-danger");
  else toastEl.classList.add("bg-warning");

  // Inicializar toast de Bootstrap
  const toast = new bootstrap.Toast(toastEl, { delay: 3000 });
  toast.show();
}

function hideToast() {
  const toastEl = document.getElementById("toast");
  const toast = bootstrap.Toast.getInstance(toastEl);
  if (toast) toast.hide();
}

// Detectar parámetros en la URL
document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  const status = params.get("status");
  const msg = params.get("msg");

  if (status && msg) {
    const decodedMsg = decodeURIComponent(msg);
    showToast(decodedMsg, status);
  }
});

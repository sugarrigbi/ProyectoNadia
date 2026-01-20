document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const usuario = document.getElementById("usuario").value;
  const password = document.getElementById("password").value;

  const res = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ usuario, password }),
  });

  const data = await res.json();
  if (data.status === "success") {
    window.location.href = data.redirect; // "/admin" o "/user"
  } else {
    document.getElementById("msg").textContent = "Credenciales inválidas";
  }
});
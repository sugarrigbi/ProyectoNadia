// static/js/scroll.js
// static/js/scroll.js
(function () {
  const NAVBAR_OFFSET = 80; // ajusta este valor según la altura de tu navbar

  function smoothScrollToId(id) {
    const el = document.getElementById(id);
    if (el) {
      const yOffset = -NAVBAR_OFFSET; 
      const y = el.getBoundingClientRect().top + window.scrollY + yOffset;

      window.scrollTo({
        top: y,
        behavior: "smooth"
      });

      history.pushState(null, "", "#" + id);
    }
  }

  // Manejar clicks en enlaces hash (por ejemplo <a href="#servicios">)
  document.addEventListener("click", function (e) {
    const a = e.target.closest("a");
    if (!a) return;
    const href = a.getAttribute("href") || "";
    if (href.startsWith("#") && href.length > 1) {
      e.preventDefault();
      const id = href.substring(1);
      smoothScrollToId(id);
    }
  });

  // Al cargar la página con hash desde una ruta externa
  window.addEventListener("load", function () {
    const hash = location.hash;
    if (hash && hash.length > 1) {
      const id = hash.substring(1);
      setTimeout(() => smoothScrollToId(id), 150);
    }
  });
})();

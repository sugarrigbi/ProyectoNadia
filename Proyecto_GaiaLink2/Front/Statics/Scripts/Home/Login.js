document.addEventListener("DOMContentLoaded", () => {
    const token = localStorage.getItem("Auth_Token") || sessionStorage.getItem("Auth_Token");
    if (token){
        window.location.href = "/dashboard";
    }
});
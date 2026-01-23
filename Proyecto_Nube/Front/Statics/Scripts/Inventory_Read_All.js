document.addEventListener("DOMContentLoaded", () => {
    const selectAll = document.getElementById("selectAll");
    const deleteBtn = document.getElementById("deleteSelected");
    const children = document.querySelectorAll(".selectChild");
    selectAll.addEventListener("change", function() {
        children.forEach(child => {
            child.checked = this.checked;
        });
    });
    children.forEach(child => {
        child.addEventListener("change", function() {
            selectAll.checked = Array.from(children).every(c => c.checked);
        });
    });
    deleteBtn.addEventListener("click", () => {
        const checkboxes = document.querySelectorAll(".selectChild:checked");
        const selectedIds = Array.from(checkboxes).map(cb => cb.value);

        if(selectedIds.length === 0){
            alert("No seleccionaste ningún libro");
            return;
        }

        const form = document.createElement("form");
        form.method = "POST";
        form.action = "/Inventory/Books/Delete/Selected";

        selectedIds.forEach(id => {
            const input = document.createElement("input");
            input.type = "hidden";
            input.name = "selected_books";
            input.value = id;
            form.appendChild(input);
        });

        document.body.appendChild(form);
        form.submit();
    });    
});
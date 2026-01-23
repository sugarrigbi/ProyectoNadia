from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__,template_folder="Templates",static_folder="Statics")

API_URL = "http://127.0.0.1:5000/"

@app.route("/Dashboard")
def Dashboard():
    return render_template("Dashboard.html", Books="a", Datos="e")
@app.route("/Catalog/Books/Read/All")
def App_Books_Read_All():
    Status = request.args.get("Status")

    Response = requests.get(API_URL+"Catalog/Books/Read/All")
    Books = Response.json()
    return render_template("Books_Read_All.html", Books=Books, Datos = {}, Status=Status)
@app.route("/Catalog/Books/Read/Search")
def App_Books_Read_By():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    Datos = {"Field": Field, "Value": Value}
    Response = requests.get(API_URL+f"Catalog/Books/Read/Search?Field={Field}&Value={Value}")
    Books = Response.json()
    return render_template("Books_Read_All.html", Books=Books, Datos=Datos)
@app.route("/Catalog/Books/Delete/<int:Book_Id>")
def App_Books_Delete(Book_Id):
    Response = requests.delete(API_URL+f"Catalog/Books/Delete/{Book_Id}")
    if Response.status_code == 400:
        return redirect(url_for("App_Books_Read_All", Status="Error"))
    elif Response.status_code == 200:
        return redirect(url_for("App_Books_Read_All", Status="Success"))
    return redirect(url_for("App_Books_Read_All"))
@app.route("/Catalog/Books/Delete/Selected", methods=["POST"])
def App_Books_Delete_Selected():
    selected_ids = request.form.getlist("selected_books")
    selected_ids = [int(i) for i in selected_ids]
    Response = requests.post(API_URL+f"Catalog/Books/Delete/Selected", json=selected_ids)
    return redirect(url_for("App_Books_Read_All"))
@app.route("/Catalog/Books/Update/<int:Book_Id>", methods=["POST"])
def App_Books_Update(Book_Id):
    Datos = {
        "Autores": request.form["Autores"],
        "Año": request.form["Año"],
        "Páginas": request.form["Páginas"],
        "Idioma": request.form["Idioma"],
        "Editorial": request.form["Editorial"],
        "Categoría": request.form["Categoría"]
    }
    Response = requests.put(API_URL+f"Catalog/Books/Update/{Book_Id}", json=Datos)

    if Response.status_code == 400:
        return redirect(url_for("App_Books_Read_All", Status2="Error"))
    elif Response.status_code == 200:
        return redirect(url_for("App_Books_Read_All", Status2="Success"))  
    return redirect(url_for("App_Books_Read_All"))  
@app.route("/Inventory/Books/Read/All")
def App_Inventory_Read_All():
    Status = request.args.get("Status")

    Response = requests.get(API_URL+"Inventory/Books/Read/All")
    Books = Response.json()
    return render_template("Inventory_Read_All.html", Books=Books, Datos = {}, Status=Status)
@app.route("/Inventory/Books/Read/Search")
def App_Inventory_Read_By():
    Field = request.args.get("Field")
    Value = request.args.get("Value")
    Datos = {"Field": Field, "Value": Value}
    Response = requests.get(API_URL+f"Inventory/Books/Read/Search?Field={Field}&Value={Value}")
    Books = Response.json()
    return render_template("Inventory_Read_All.html", Books=Books, Datos=Datos)
@app.route("/Inventory/Books/Delete/<int:Book_Id>")
def App_Inventory_Delete(Book_Id):
    Response = requests.delete(API_URL+f"Inventory/Books/Delete/{Book_Id}")
    if Response.status_code == 400:
        return redirect(url_for("App_Inventory_Read_All", Status="Error"))
    elif Response.status_code == 200:
        return redirect(url_for("App_Inventory_Read_All", Status="Success"))
    return redirect(url_for("App_Inventory_Read_All"))
@app.route("/Inventory/Books/Delete/Selected", methods=["POST"])
def App_Inventory_Delete_Selected():
    selected_ids = request.form.getlist("selected_books")
    selected_ids = [int(i) for i in selected_ids]
    Response = requests.post(API_URL+f"Inventory/Books/Delete/Selected", json=selected_ids)
    return redirect(url_for("App_Inventory_Read_All"))
@app.route("/Inventory/Books/Update/<int:Book_Id>", methods=["POST"])
def App_Inventory_Update(Book_Id):
    Datos = {
        "Quantity": int(request.form["Quantity"]),
        "Fk_Status": request.form["Fk_Status"],
        "Fk_Book": int(request.form["Fk_Book"]),
        "Fk_Location": request.form["Fk_Location"]
    }
    Response = requests.put(API_URL+f"Inventory/Books/Update/{Book_Id}", json=Datos)

    if Response.status_code == 400:
        return redirect(url_for("App_Inventory_Read_All", Status2="Error"))
    elif Response.status_code == 200:
        return redirect(url_for("App_Inventory_Read_All", Status2="Success"))  
    return redirect(url_for("App_Inventory_Read_All"))  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)



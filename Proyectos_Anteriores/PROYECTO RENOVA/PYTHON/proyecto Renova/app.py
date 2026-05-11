from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("sitio_web/pagina/index.html")


@app.route("/que_es_renova")
def que_es_renova():
    return render_template("sitio_web/pagina/que_es_renova.html")


@app.route("/informacion")
def informacion():
    return render_template("sitio_web/pagina/informacion.html")


@app.route("/mision")
def mision():
    return render_template("sitio_web/pagina/mision.html")


@app.route("/vision")
def vision():
    return render_template("sitio_web/pagina/vision.html")


@app.route("/objetivos")
def objetivos():
    return render_template("sitio_web/pagina/objetivos.html")


@app.route("/servicios")
def servicios():
    return render_template("sitio_web/pagina/servicios.html")


@app.route("/contacto")
def contacto():
    return render_template("sitio_web/pagina/contacto.html")


# BUSCADOR
@app.route("/buscar")
def buscar():
    query = request.args.get("q")

    if not query:
        return redirect(url_for("inicio"))

    query = query.lower()

    rutas = {
        "inicio": "inicio",
        "renova": "que_es_renova",
        "informacion": "informacion",
        "mision": "mision",
        "vision": "vision",
        "objetivos": "objetivos",
        "servicios": "servicios",
        "contacto": "contacto"
    }

    for palabra, ruta in rutas.items():
        if palabra in query:
            return redirect(url_for(ruta))

    return render_template("sitio_web/pagina/no_encontrado.html", busqueda=query)


if __name__ == '__main__':
    app.run(debug=True)
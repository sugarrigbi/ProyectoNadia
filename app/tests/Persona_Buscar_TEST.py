import pytest
from app.models.Persona import app

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente

def test_get_persona_found(monkeypatch, cliente):
    # Simulamos que Buscar_Persona devuelve datos
    fake_data = {
        "Codigo": "001",
        "Tipo_Documento": "CC",
        "Documento": "12345",
        "Primer_Nombre": "Juan",
        "Segundo_Nombre": "Carlos",
        "Primer_Apellido": "Pérez",
        "Segundo_Apellido": "López",
        "Fecha_Nacimiento": "01/01/2000",
        "Codigo_Adic": "A1",
        "Edad": 25,
        "Direccion": "Calle Falsa 123",
        "Departamento": "Cundinamarca",
        "Ciudad": "Bogotá",
        "Localidad": "Suba",
        "Barrio": "Los Nogales",
        "Numero_Contacto": "3001234567",
        "Email": "juan@example.com",
        "Nombre": "Sugarrigbi",
        "Contraseña": "12345",
        "Rol": "Usu",
        "Estado": "0"
    }

    from app.models.Persona import Persona
    monkeypatch.setattr(Persona, "Buscar_Persona", lambda self: fake_data)

    response = cliente.get("/personas/12345")

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["Primer_Nombre"] == "Juan"
    assert json_data["Edad"] == 25

def test_get_persona_not_found(monkeypatch, cliente):
    from app.models.Persona import Persona
    monkeypatch.setattr(Persona, "Buscar_Persona", lambda self: None)

    response = cliente.get("/personas/99999")

    assert response.status_code == 404
    json_data = response.get_json()
    assert "Usuario no encontrado" in json_data["error"]

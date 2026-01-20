import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, session, request
from app.controler.controler import Consulta

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.secret_key = 'testkey'
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@patch('app.controler.controler.Usuario.get_user_by_session')
@patch('app.controler.controler.Caso.get_cases_user')
def test_buscar_caso_usuario(mock_get_cases_user, mock_get_user, client):
    mock_get_user.return_value = 1
    mock_get_cases_user.return_value = [{"id": 1, "caso": "Caso prueba"}]
    consulta = Consulta()
    casos = consulta.buscar_caso_usuario()
    assert casos == [{"id": 1, "caso": "Caso prueba"}]

@patch('app.controler.controler.Caso.get_cases_admin')
def test_buscar_casos_admin(mock_get_cases_admin):
    mock_get_cases_admin.return_value = [{"id": 1, "caso": "Caso admin"}]
    consulta = Consulta()
    casos = consulta.buscar_casos_admin()
    assert casos == [{"id": 1, "caso": "Caso admin"}]

@patch('app.controler.controler.Usuario.get_user_by_session')
@patch('app.controler.controler.Usuario.get_user_account')
def test_ver_datos_usuario(mock_get_account, mock_get_user, app):
    mock_get_user.return_value = 1
    mock_get_account.return_value = {"contrasena": "123456", "nombre": "Kevin"}
    consulta = Consulta()
    with app.test_request_context():
        session['username'] = 'Kevin'
        resp = consulta.ver_datos_usuario()
        data = resp.get_json()
        assert data["contrasena_masked"].endswith("56")
        assert data["nombre"] == "Kevin"

@patch('app.controler.controler.Usuario.get_all_users')
def test_obtener_usuarios(mock_get_all_users, app):
    mock_get_all_users.return_value = [(1, "Kevin"), (2, "Sara")]
    consulta = Consulta()
    with app.test_request_context():
        resp = consulta.obtener_usuarios()
        data = resp.get_json()
        assert len(data) == 2
        assert data[0]["nombre"] == "Kevin"

@patch('app.controler.controler.Caso.generate_report')
def test_generar_reporte(mock_generate_report, app):
    mock_generate_report.return_value = [{"id": 1, "caso": "Caso reporte"}]
    consulta = Consulta()
    with app.test_request_context(method='POST', data={"FechaInicial":"2025-10-01","FechaFinal":"2025-10-10"}):
        resp = consulta.generar_reporte()
        if isinstance(resp, tuple):
            data, code = resp
            assert code == 200
        else:
            assert resp.status_code == 200

def test_generar_reporte_fechas_invalidas(app):
    consulta = Consulta()
    with app.test_request_context(method='POST', data={"FechaInicial":"2025-10-10","FechaFinal":"2025-10-01"}):
        resp, code = consulta.generar_reporte()
        assert code == 400
        data = resp.get_json()
        assert "La fecha inicial no puede ser mayor" in data["msg"]

def test_generar_reporte_faltan_datos(app):
    consulta = Consulta()
    with app.test_request_context(method='POST', data={}):
        resp, code = consulta.generar_reporte()
        assert code == 400
        data = resp.get_json()
        assert "Faltan datos" in data["msg"]

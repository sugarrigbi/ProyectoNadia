import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, session, request
from app.controler.controler import Registro

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.secret_key = 'testkey'
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@patch('app.controler.controler.url_for')
@patch('app.controler.controler.Usuario.username_exists')
@patch('app.controler.controler.Usuario.documento_exists')
@patch('app.controler.controler.Usuario.email_exist')
@patch('app.controler.controler.Usuario.insert_user_with_details')
@patch('app.controler.controler.enviar_correo_registro')
def test_registro_exitoso(mock_correo, mock_insert_user, mock_email_exist, mock_doc_exist, mock_username_exist, mock_url_for, app):
    mock_url_for.return_value = "/user/dashboard"
    mock_username_exist.return_value = False
    mock_doc_exist.return_value = False
    mock_email_exist.return_value = False

    registro = Registro()
    data = {
        "username": "Kevin01",
        "password": "Passw0rd!",
        "documento": "123456",
        "primer_nombre": "Kevin",
        "segundo_nombre": "Andres",
        "primer_apellido": "Anzola",
        "segundo_apellido": "García",
        "tipo_documento": "CC",
        "fecha_nacimiento": "2000-01-01",
        "edad": "25",
        "direccion": "Calle 123",
        "telefono": "3001234567",
        "email": "kevin@test.com"
    }

    with app.test_request_context(method='POST', data=data):
        resp = registro.registro()
        assert resp.status_code == 302
        assert resp.location == "/user/dashboard"

@patch('app.controler.controler.Usuario.get_user_by_session')
@patch('app.controler.controler.Caso.insert_case')
@patch('app.controler.controler.Caso.get_case_by_id')
@patch('app.controler.controler.Usuario.get_user_account')
@patch('app.controler.controler.enviar_correo_caso')
def test_registrar_caso_usuario_exitoso(mock_correo, mock_get_user_account, mock_get_case, mock_insert_case, mock_get_user_session, app):
    mock_get_user_session.return_value = 1
    mock_insert_case.return_value = 10
    mock_get_user_account.return_value = {"email": "kevin@test.com", "nombres": "Kevin", "apellidos": "Anzola"}
    mock_get_case.return_value = {"desastre": "Inundación"}

    registro = Registro()
    data = {
        "fecha": "2025-10-15",
        "descripcion": "Prueba caso",
        "direccion": "Calle 123",
        "personas_afectadas": "3",
        "tipo_desastre": "1",
        "ciudad": "1"
    }

    with app.test_request_context(method='POST', data=data):
        resp = registro.registrar_caso_usuario()
        assert resp[1] == 200
        json_data = resp[0].get_json()
        assert json_data["status"] == "success"

def test_registrar_caso_usuario_faltan_datos(app):
    registro = Registro()
    data = {
        "fecha": "",
        "descripcion": "",
        "direccion": "",
        "personas_afectadas": "",
        "tipo_desastre": "",
        "ciudad": ""
    }
    with app.test_request_context(method='POST', data=data):
        resp, code = registro.registrar_caso_usuario()
        assert code == 400
        json_data = resp.get_json()
        assert "complete todos los campos" in json_data["msg"]

def test_registrar_caso_usuario_personas_afectadas_invalidas(app):
    registro = Registro()
    data = {
        "fecha": "2025-10-15",
        "descripcion": "Prueba",
        "direccion": "Calle 123",
        "personas_afectadas": "30",
        "tipo_desastre": "1",
        "ciudad": "1"
    }
    with app.test_request_context(method='POST', data=data):
        resp, code = registro.registrar_caso_usuario()
        assert code == 400
        json_data = resp.get_json()
        assert "número de personas afectadas" in json_data["msg"]

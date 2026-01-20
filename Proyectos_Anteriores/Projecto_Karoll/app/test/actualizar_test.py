import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, request
from app.controler.controler import Actualizar
from flask import session, jsonify

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.secret_key = 'testkey'
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@patch('app.models.usuario.Usuario.get_user_by_session', return_value=None)
def test_actualizar_usuario_no_sesion(mock_session, app):
    actualizar = Actualizar()
    with app.test_request_context(method='POST', data={}):
        resp, code = actualizar.actualizar_datos_usuario()
        assert code == 500
        data = resp.get_json()
        assert data['status'] == 'error'

@patch('app.models.usuario.Usuario.get_user_by_session', return_value=1)
def test_actualizar_sin_campos(mock_session, app):
    actualizar = Actualizar()
    with app.test_request_context(method='POST', data={}):
        resp, code = actualizar.actualizar_datos_usuario()
        assert code == 400
        data = resp.get_json()
        assert data['status'] == 'warning'
        assert "Debe proporcionar al menos un campo" in data['msg']

@patch('app.models.usuario.Usuario.get_user_by_session', return_value=1)
@patch('app.models.usuario.Usuario.username_exists', return_value=True)
def test_actualizar_usuario_existente(mock_username, mock_session, app):
    actualizar = Actualizar()
    with app.test_request_context(method='POST', data={'username':'existente'}):
        resp, code = actualizar.actualizar_datos_usuario()
        assert code == 400
        data = resp.get_json()
        assert data['status'] == 'error'

@patch('app.models.usuario.Usuario.get_user_by_session', return_value=1)
@patch('app.models.usuario.Usuario.username_exists', return_value=False)
def test_actualizar_edad_invalida(mock_username, mock_session, app):
    actualizar = Actualizar()
    with app.test_request_context(method='POST', data={'edad':'abc'}):
        resp, code = actualizar.actualizar_datos_usuario()
        assert code == 400
        data = resp.get_json()
        assert "número válido" in data['msg']
    with app.test_request_context(method='POST', data={'edad':'17'}):
        resp, code = actualizar.actualizar_datos_usuario()
        data = resp.get_json()
        assert code == 400
        assert "entre 18 y 90 años" in data['msg']

@patch('app.models.usuario.Usuario.get_user_by_session', return_value=1)
def test_actualizar_telefono_invalido(mock_session, app):
    actualizar = Actualizar()
    with app.test_request_context(method='POST', data={'telefono':'123'}):
        resp, code = actualizar.actualizar_datos_usuario()
        data = resp.get_json()
        assert code == 400
        assert "número de teléfono debe ser válido" in data['msg']

@patch('flask.templating.render_template', return_value="correo simulado")
@patch('app.models.usuario.Usuario.get_user_by_session', return_value=1)
@patch('app.models.usuario.Usuario.update_user_account', return_value=True)
@patch('app.models.usuario.Usuario.get_user_account')
@patch('app.models.utils.enviar_correo_actualización_datos')
def test_actualizar_exito(mock_render, mock_email, mock_get_user, mock_update, mock_session, app):
    mock_get_user.return_value = {
        'nombres':'Tatiana',
        'apellidos':'Perez',
        'direccion':'Calle 1',
        'email':'test@test.com',
        'telefono':'3001234567',
        'edad':30,
        'nombre_usuario':'testuser'
    }
    actualizar = Actualizar()
    with app.test_request_context(method='POST', data={'pri_nom':'Tatiana','edad':'30'}):
        resp, code = actualizar.actualizar_datos_usuario()
        data = resp.get_json()
        assert code == 200
        assert data['status'] == 'success'
        mock_email.assert_called_once()

@patch('app.models.usuario.Usuario.get_user_by_session', return_value=1)
@patch('app.models.usuario.Usuario.update_user_account', return_value=False)
def test_actualizar_error_db(mock_update, mock_session, app):
    actualizar = Actualizar()
    with app.test_request_context(method='POST', data={'pri_nom':'Tatiana'}):
        resp, code = actualizar.actualizar_datos_usuario()
        data = resp.get_json()
        assert code == 500
        assert data['status'] == 'error'

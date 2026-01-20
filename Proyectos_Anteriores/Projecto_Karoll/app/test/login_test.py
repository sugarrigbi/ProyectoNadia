import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, session, request
from app.controler.controler import Login

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
@patch('app.controler.controler.Usuario.get_user_by_name')
def test_login_exitoso_usuario(mock_get_user, mock_url_for, app):
    mock_url_for.return_value = "/user/dashboard"
    user_mock = MagicMock()
    user_mock.username = "Kevin01"
    user_mock.password = "Passw0rd!"
    user_mock.estado = "01"
    user_mock.rol = "Usuario"
    mock_get_user.return_value = user_mock

    login = Login()
    data = {"username": "Kevin01", "password": "Passw0rd!"}
    with app.test_request_context(method='POST', data=data):
        resp = login.login()
        assert resp.status_code == 302
        assert resp.location == "/user/dashboard"
        assert session['username'] == "Kevin01"

@patch('app.controler.controler.url_for')
@patch('app.controler.controler.Usuario.get_user_by_name')
def test_login_exitoso_admin(mock_get_user, mock_url_for, app):
    mock_url_for.return_value = "/admin/dashboard"
    user_mock = MagicMock()
    user_mock.username = "Admin01"
    user_mock.password = "AdminPass!"
    user_mock.estado = "01"
    user_mock.rol = "Admin"
    mock_get_user.return_value = user_mock

    login_instance = Login()
    data = {"username": "Admin01", "password": "AdminPass!"}
    with app.test_request_context(method='POST', data=data):
        resp = login_instance.login()
        assert resp.status_code == 302
        assert resp.location == "/admin/dashboard"
        assert session['username'] == "Admin01"

@patch('app.controler.controler.url_for')
@patch('app.controler.controler.Usuario.get_user_by_name')
def test_login_usuario_no_encontrado(mock_get_user, mock_url_for, app):
    mock_url_for.return_value = "/auth/login"
    mock_get_user.return_value = None
    login_instance = Login()
    data = {"username": "Inexistente", "password": "abc123!"}
    with app.test_request_context(method='POST', data=data):
        resp = login_instance.login()
        assert resp.status_code == 302
        assert resp.location == "/auth/login"

@patch('app.controler.controler.url_for')
@patch('app.controler.controler.Usuario.get_user_by_name')
def test_login_contraseña_incorrecta(mock_get_user, mock_url_for, app):
    mock_url_for.return_value = "/auth/login"
    user_mock = MagicMock()
    user_mock.username = "Kevin01"
    user_mock.password = "Passw0rd!"
    user_mock.estado = "01"
    user_mock.rol = "Usuario"
    mock_get_user.return_value = user_mock

    login_instance = Login()
    data = {"username": "Kevin01", "password": "WrongPass!"}
    with app.test_request_context(method='POST', data=data):
        resp = login_instance.login()
        assert resp.status_code == 302
        assert resp.location == "/auth/login"

@patch('app.controler.controler.url_for')
@patch('app.controler.controler.Usuario.get_user_by_name')
def test_login_usuario_inactivo(mock_get_user, mock_url_for, app):
    mock_url_for.return_value = "/auth/login"
    user_mock = MagicMock()
    user_mock.username = "Kevin01"
    user_mock.password = "Passw0rd!"
    user_mock.estado = "00"
    user_mock.rol = "Usuario"
    mock_get_user.return_value = user_mock

    login_instance = Login()
    data = {"username": "Kevin01", "password": "Passw0rd!"}
    with app.test_request_context(method='POST', data=data):
        resp = login_instance.login()
        assert resp.status_code == 302
        assert resp.location == "/auth/login"

@patch('app.controler.controler.url_for')
def test_logout(mock_url_for, app):
    mock_url_for.return_value = "/auth/login"
    login_instance = Login()
    with app.test_request_context():
        session['username'] = "Kevin01"
        session['user_id'] = 1
        session['rol'] = "Usuario"
        resp = login_instance.logout()
        assert resp.status_code == 302
        assert resp.location == "/auth/login"
        assert 'username' not in session
        assert 'user_id' not in session
        assert 'rol' not in session

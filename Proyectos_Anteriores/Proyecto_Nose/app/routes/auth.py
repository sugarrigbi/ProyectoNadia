# app/routes/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, session,flash
from app.models.controler import Login
from app.models.controler import Registro


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():     
    return Login().login()

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return Registro().registro()




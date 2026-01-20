# app/__init__.py
from flask import Flask, render_template, session
from app.routes.auth import auth_bp
from app.routes.admin import admin_bp
from app.routes.user import user_bp
from app.extensions import mail
from dotenv import load_dotenv
import os


def create_app():
    
    app = Flask(__name__)
    app.secret_key = 'VitariaSOSAuthenticated'  
     
    load_dotenv()
    
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
    
    mail.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    return app

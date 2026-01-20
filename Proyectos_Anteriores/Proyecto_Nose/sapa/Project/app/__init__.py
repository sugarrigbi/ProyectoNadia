# app/__init__.py
from flask import Flask, render_template, session
from app.routes.auth import auth_bp
from app.routes.admin import admin_bp
from app.routes.user import user_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'tu_clave_secreta'  # Clave simple para sesiones (cambia para seguridad mínima)

    # Registrar blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
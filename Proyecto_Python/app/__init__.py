from flask import Flask
from datetime import timedelta
from app.routes.routes import routes_bp
from app.routes.home import home_bp
from app.routes.login import auth_bp
from app.routes.formularios import form_bp
from app.routes.user import user_bp
from app.routes.admin import admin_bp

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SECRET_KEY'] = '1145224601Aa'
    app.permanent_session_lifetime = timedelta(days=7)

    app.register_blueprint(auth_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(form_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)

    return app
from flask import Flask
from app.routes.routes import routes_bp
from app.routes.home import home_bp
from app.routes.login import auth_bp
from app.routes.formularios import form_bp
from app.routes.user import user_bp
def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SECRET_KEY'] = '1145224601Aa'
    app.permanent_session_lifetime = 60 * 60 * 24 * 30

    app.register_blueprint(auth_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(form_bp)
    app.register_blueprint(user_bp)

    return app
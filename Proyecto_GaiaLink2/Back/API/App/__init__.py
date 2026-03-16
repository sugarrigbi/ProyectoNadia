from flask import Flask, render_template, jsonify, request
from App.Routes.Forms_Service import Forms_Service_Bp
from App.Routes.User_Service import User_Service_Bp
from App.Routes.Auth_Service import Auth_Service_Bp
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def Create_App():
    App = Flask(__name__)

    Rate_Limit = Limiter(
        get_remote_address,
        app=App,
        default_limits=["5 per minute"],
        storage_uri="redis://localhost:6379"
    )
    @App.errorhandler(429)
    def ratelimit_handler(e):
        if request.path.startswith("/api/"):
            return jsonify(error="Demasiadas solicitudes"), 429
        else:
            return render_template("Rate_Limit.html", mensaje="Has excedido el número de intentos permitidos"), 429

    CORS(App, resources={r"/api/*": {"origins": 
    [
        "http://localhost:5009",
        "https://p8kjdpww-5009.use2.devtunnels.ms"
    ]
    }}, supports_credentials=True, allow_headers=["Content-Type", "Authorization", "X-Requested-With"])

    App.register_blueprint(Forms_Service_Bp)
    App.register_blueprint(User_Service_Bp)
    App.register_blueprint(Auth_Service_Bp)

    return App 
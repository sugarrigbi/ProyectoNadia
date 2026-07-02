from App.Routes.Authenticator_Service import Auth_Service_Bp
from App.Routes.Account_Service import Account_Service_Bp
from App.Routes.Entity_Service import Entity_Service_Bp
from App.Routes.Health_Service import Health_Service_Bp
from App.Routes.Forms_Service import Forms_Service_Bp
from App.Routes.User_Service import User_Service_Bp
from App.Routes.Case_Service import Case_Service_Bp
from flask import Flask, jsonify, request
from App.Rate_Limit import Rate_Limit
from flask_cors import CORS
import os

def Create_App():
    App = Flask(__name__)

    Rate_Limit.init_app(App)
    @App.errorhandler(429)
    def ratelimit_handler(e):
        return jsonify(error="Demasiadas solicitudes"), 429
    
    @App.before_request
    def skip_options():
        if request.method == "OPTIONS":
            Respuesta = App.make_response("")
            Respuesta.status_code = 200
            Respuesta.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "*")
            Respuesta.headers["Access-Control-Allow-Credentials"] = "true"
            Respuesta.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
            Respuesta.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
            return Respuesta
    
    CORS(
        App,
        resources={
            r"/*": {
                "origins": os.getenv("CORS_ORIGINS").split(","),
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"]
            }
        },
        supports_credentials=True,
        expose_headers=["Content-Disposition"]
    )

    App.register_blueprint(Forms_Service_Bp)
    App.register_blueprint(User_Service_Bp)
    App.register_blueprint(Auth_Service_Bp)
    App.register_blueprint(Case_Service_Bp)
    App.register_blueprint(Entity_Service_Bp)
    App.register_blueprint(Account_Service_Bp)
    App.register_blueprint(Health_Service_Bp)

    return App 
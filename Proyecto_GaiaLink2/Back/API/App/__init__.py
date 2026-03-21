from flask import Flask, render_template, jsonify, request
from App.Routes.Forms_Service import Forms_Service_Bp
from App.Routes.User_Service import User_Service_Bp
from App.Routes.Auth_Service import Auth_Service_Bp
from App.Routes.Case_Service import Case_Service_Bp
from flask_cors import CORS
from App.Rate_Limit import Rate_Limit

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
            r"/api/*": {
                "origins": [
                    "http://localhost:5009",
                    "https://p8kjdpww-5009.use2.devtunnels.ms"
                ],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"]
            }
        },
        supports_credentials=True
    )


    App.register_blueprint(Forms_Service_Bp)
    App.register_blueprint(User_Service_Bp)
    App.register_blueprint(Auth_Service_Bp)
    App.register_blueprint(Case_Service_Bp)

    return App 
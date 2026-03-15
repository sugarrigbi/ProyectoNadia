from flask import Flask
from App.Routes.Forms_Service import Forms_Service_Bp
from App.Routes.User_Service import User_Service_Bp
from App.Routes.Auth_Service import Auth_Service_Bp
from flask_cors import CORS

def Create_App():
    App = Flask(__name__)

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
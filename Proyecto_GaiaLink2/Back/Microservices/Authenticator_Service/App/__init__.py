from flask import Flask
from App.Routes.Autenticator_Routes import Auth_Service_Bp
from App.Utilities.Tables import  db
from App.Config import Config

def Create_App():
    App = Flask(__name__)

    App.config.from_object(Config)
    db.init_app(App)

    App.register_blueprint(Auth_Service_Bp)

    return App

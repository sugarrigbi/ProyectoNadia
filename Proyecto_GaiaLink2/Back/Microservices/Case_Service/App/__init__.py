from flask import Flask
from App.Routes.Case_Routes import Case_Bp
from App.Config import Config
from App.Utilities.Extension import db

def Create_App():
    App = Flask(__name__)
    App.config.from_object(Config)

    db.init_app(App)

    App.register_blueprint(Case_Bp)

    return App
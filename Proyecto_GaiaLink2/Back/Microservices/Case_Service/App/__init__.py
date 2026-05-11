from App.Routes.Case_Routes import Case_Bp
from App.Utilities.Tables import db
from App.Config import Config
from flask import Flask

def Create_App():
    App = Flask(__name__)
    
    App.config.from_object(Config)
    db.init_app(App)

    App.register_blueprint(Case_Bp)

    return App


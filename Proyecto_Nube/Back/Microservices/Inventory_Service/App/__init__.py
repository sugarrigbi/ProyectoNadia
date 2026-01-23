from flask import Flask
from App.Routes.Inventory_Routes import Inventory_Bp
from App.Config import Config
from App.Utilities.Extension import db

def Create_App():
    App = Flask(__name__)
    App.config.from_object(Config)

    db.init_app(App)

    App.register_blueprint(Inventory_Bp, url_prefix="/Inventory")

    return App
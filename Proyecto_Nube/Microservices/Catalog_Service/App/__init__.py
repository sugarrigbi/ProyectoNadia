from flask import Flask
from App.Routes.Catalog_Routes import Catalog_Bp
from App.Config import Config
from App.Utilities.Extension import db

def Create_App():
    App = Flask(__name__)
    App.config.from_object(Config)

    db.init_app(App)

    App.register_blueprint(Catalog_Bp, url_prefix="/Catalog")

    return App
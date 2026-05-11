from App.Routes.Forms_Routes import Forms_Bp
from App.Utilities.Tables import db
from App.Config import Config
from flask import Flask

def Create_App():
    App = Flask(__name__)

    App.config.from_object(Config)
    db.init_app(App)

    App.register_blueprint(Forms_Bp)

    return App
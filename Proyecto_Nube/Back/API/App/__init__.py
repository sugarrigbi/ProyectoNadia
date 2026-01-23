from flask import Flask
from App.Routes.Catalog_Proxy_Routes import Catalog_Bp
from App.Routes.Inventoy_Proxy_Routes import Inventory_Bp
from flask_cors import CORS
def Create_App():
    app = Flask(__name__, template_folder="Front/Templates",static_folder="Front/Statics")
    CORS(app)
    app.register_blueprint(Catalog_Bp)
    app.register_blueprint(Inventory_Bp)
    return app
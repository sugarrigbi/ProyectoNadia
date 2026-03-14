from flask import Flask
from App.Routes.Notification_Routes import Notification_Service_Bp

app = Flask(__name__)

app.register_blueprint(Notification_Service_Bp)

if __name__ == "__main__":
    app.run(debug=True, port=5007)
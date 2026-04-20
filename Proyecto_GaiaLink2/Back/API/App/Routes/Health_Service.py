from App.Routes.Account_Service import MICROSERVICE_URL as ACCOUNT_URL
from App.Routes.Authenticator_Service import MICROSERVICE_URL as AUTHENTICATOR_URL
from App.Routes.Case_Service import MICROSERVICE_URL as CASE_URL
from App.Routes.Entity_Service import MICROSERVICE_URL as ENTITY_URL
from App.Routes.Forms_Service import MICROSERVICE_URL as FORMS_URL
from App.Routes.Notification_Service import MICROSERVICE_URL as NOTIFICATION_URL
from App.Routes.User_Service import MICROSERVICE_URL as USER_URL
from flask import Blueprint, jsonify
import requests
from datetime import datetime
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT

Health_Service_Bp = Blueprint("Health_Service", __name__)

@Health_Service_Bp.route("/api/health", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Health_Check():
    try:
        Account = requests.get(f"{ACCOUNT_URL}/account/health", timeout=3)
        Account_Status = "OK" if Account.status_code == 200 else "OFF"
    except:
        Account_Status = "OFF"
    try:
        Authenticator = requests.get(f"{AUTHENTICATOR_URL}/health", timeout=3)
        Authenticator_Status = "OK" if Authenticator.status_code == 200 else "OFF"
    except:
        Authenticator_Status = "OFF"
    try:
        Case = requests.get(f"{CASE_URL}/health", timeout=3)
        Case_Status = "OK" if Case.status_code == 200 else "OFF"
    except:
        Case_Status = "OFF"
    try:
        Entity = requests.get(f"{ENTITY_URL}/health", timeout=3)
        Entity_Status = "OK" if Entity.status_code == 200 else "OFF"
    except:
        Entity_Status = "OFF"
    try:
        Forms = requests.get(f"{FORMS_URL}/health", timeout=3)
        Forms_Status = "OK" if Forms.status_code == 200 else "OFF"
    except:
        Forms_Status = "OFF"
    try:
        Notification = requests.get(f"{NOTIFICATION_URL}/health", timeout=3)
        Notification_Status = "OK" if Notification.status_code == 200 else "OFF"
    except:
        Notification_Status = "OFF"
    try:
        User = requests.get(f"{USER_URL}/health", timeout=3)
        User_Status = "OK" if User.status_code == 200 else "OFF"
    except:
        User_Status = "OFF"

    return jsonify({
        "API": "OK",
        "Account": Account_Status,
        "Authenticator": Authenticator_Status,
        "Case": Case_Status,
        "Entity": Entity_Status,
        "Forms": Forms_Status,
        "Notification": Notification_Status,
        "User": User_Status,
        "ZTime": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }), 200




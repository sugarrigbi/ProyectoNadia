from App.Rate_Limit import Rate_Limit
from flask import Blueprint, jsonify
from datetime import datetime
import requests
import os

Health_Service_Bp = Blueprint("Health_Service", __name__)

USER_URL = os.getenv("USER_URL")
NOTIFICATION_URL = os.getenv("NOTIFICATION_URL")
FORMS_URL = os.getenv("FORMS_URL")
ENTITY_URL = os.getenv("ENTITY_URL")
AUTHENTICATOR_URL = os.getenv("AUTHENTICATOR_URL")
CASE_URL = os.getenv("CASE_URL")
ACCOUNT_URL = os.getenv("ACCOUNT_URL")
DEFAULT_LIMIT = os.getenv("DEFAULT_LIMIT")

@Health_Service_Bp.route("/health", methods=["GET"])
@Rate_Limit.limit(DEFAULT_LIMIT, methods=["GET"])
def Health_Check():
    try:
        Account = requests.get(f"{ACCOUNT_URL}/health", timeout=3)
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




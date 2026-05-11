from flask import Blueprint
import os

Notification_Service_Bp = Blueprint("Notification_Service", __name__)

MICROSERVICE_URL = os.getenv("NOTIFICATION_URL")
from flask import Blueprint
import requests
from App.Rate_Limit import Rate_Limit, DEFAULT_LIMIT

Notification_Service_Bp = Blueprint("Notification_Service", __name__)

MICROSERVICE_URL = "http://localhost:5007/email"
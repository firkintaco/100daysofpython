OWM_API_KEY = ""
ACCOUNT_SID = ""
AUTH_TOKEN = ""
MY_PHONE = ""
ONECALL_API = "https://api.openweathermap.org/data/3.0/onecall"

import requests
from twilio.rest import Client

def send_sms() -> str:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    if is_raining():
        # Send an sms message if its raining
        message = client.messages.create(body="It's raining today, bring an umbrella!", from_="+12176263597", to=MY_PHONE)
        print(message.status)
    else:
        print("No sms sended")

def is_raining() -> bool:
    params = {
        # "lat": 58.525570,
        # "lon": 31.274193,
        "lat": 60.192059,
        "lon": 24.945831,
        "appid": OWM_API_KEY,
        "exclude": "current,minutely,daily",
        "units": "metric"
    }
    response = requests.get(ONECALL_API, params)
    response.raise_for_status()
    weather_data = response.json()
    hourly = weather_data["hourly"][:12]
    raining = False
    for hour in hourly:
        hourly_id = hour["weather"][0]["id"]
        if hourly_id < 700:
            raining = True
    return raining


send_sms()
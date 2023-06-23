URL = "http://api.open-notify.org/iss-now.json"

import requests
import datetime

# Status codes
# 1xx: Hold on
# 2xx: Here You Go
# 3xx: Go Away
# 4xx: You screwed Up
# 5xx: I Screwed Up
def get_location():
    # GET data from url
    resp = requests.get(url=URL)
    resp.raise_for_status()
    # Convert to json
    data = resp.json()

    iss_position = data.get("iss_position") # iss_position object
    longitude = float(iss_position["longitude"]) # longitude
    latitude = float(iss_position["latitude"]) #  latitude
    location_tuple = (latitude, longitude)
    # print formatted response
    print(f"International Space Station is now at position (Lat, long): {location_tuple}")

def get_people():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    number_of_peoples = data["number"]
    peoples = data["people"]
    for people in peoples:
        print(people["name"])


# get_location()
# get_people()


def sunset_api():
    parameters = {
        "lat": 61.126661,
        "lon": 25.839844,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = response.json()["results"]
    sunset = data["sunset"].split("T")[1].split(":")[0]
    sunrise = data["sunrise"].split("T")[1].split(":")[0]
    print(sunrise, sunset)

    now = datetime.datetime.now().hour
    print(now)


sunset_api()
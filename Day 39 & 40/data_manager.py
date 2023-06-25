import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_data(self):
        response = requests.get("https://api.sheety.co/3550973c1df5dd761ce83da1ac8754b8/kopio:FlightDeals/prices")
        return response.json()["prices"]

    def update_data(self, cityId, iataCode):
        data_to_put = {
            "price": {
                "iataCode": iataCode
            }
        }
        response = requests.put(f"https://api.sheety.co/3550973c1df5dd761ce83da1ac8754b8/kopio:FlightDeals/prices/{cityId}", json=data_to_put)
        return response.json()
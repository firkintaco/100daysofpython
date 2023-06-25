
import requests
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata(self, city):
        header_params = {
            "apikey": ""
        }
        search_params = {
            "term": city,
            "location_types": "airport",
            "limit": 1,
            "active_only": "true"
        }
        endpoint = "https://api.tequila.kiwi.com/locations/query"
        response = requests.get(url=endpoint, params=search_params, headers=header_params)
        return response.json()["locations"][0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"https://api.tequila.kiwi.com/v2/search",
            headers=headers,
            params=query,
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 2
            response = requests.get(
                url=f"https://api.tequila.kiwi.com/v2/search",
                headers=headers,
                params=query,
            )
            print(response.json())
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
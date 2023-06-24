import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "lassi"
TOKEN = ""

user_params = {
    "token": "",
    "username": "lassi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Push ups",
    "unit": "Reps",
    "type": "int",
    "color": "ajisai",
}

login_info = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=login_info)
# print(response)

endpoint = f"{graph_endpoint}/graph1"
quantity = input("How many you did today?:\n")
data_to_send = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": quantity
}


response = requests.post(url=endpoint, json=data_to_send, headers=login_info)
print(response.text)
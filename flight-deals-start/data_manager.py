import requests
from pprint import pprint
#SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/flightDeals/prices"

SHEETY_ENDPOINT = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}
    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    def update_destination_code(self):
        for city in self.destination_data:
            new_data={
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{city['id']}",
                                    json=new_data
                                    )
            print(response.text)


import requests
from pprint import pprint
#SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/flightDeals/prices"

SHEETY_ENDPOINT = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/flightDeals/prices"
sheety_endpoint_users = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/flightDeals/users"

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = []
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
    def customer_email(self):
        response = requests.get(sheety_endpoint_users)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data



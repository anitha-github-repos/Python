#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData
from datetime import datetime, timedelta
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"

# import requests
# from pprint import pprint
#
# sheety_endpoint = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/flightDeals/prices"
#
# response = requests.get(sheety_endpoint)
# pprint(response.json())
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    #print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

tomarrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA,destination["iataCode"], from_time=tomarrow, to_time=six_months_from_today)


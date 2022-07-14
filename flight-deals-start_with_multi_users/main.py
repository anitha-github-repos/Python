#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_data import FlightData
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
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

destinations = {
    data["iataCode"] : {
        "id" : data["id"],
        "city" : data["city"],
        "price" : data["lowestPrice"]
    }for data in sheet_data
}
tomarrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination_code in destinations:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA,destination_code, from_time=tomarrow, to_time=six_months_from_today)
    if flight is None:
        continue
    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.customer_email()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        #if flight.stop_overs > 0:
            #message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)


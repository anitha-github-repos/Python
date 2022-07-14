import requests

sheety_endpoint = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/flightDeals/users"

response = requests.get(sheety_endpoint)
print(response.json())

print("Welcome to Anitha's Flight Club\nWe find the best flight deals and email you")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
confirm_email = input("What is your email? ")
if email == confirm_email:
    json_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    print(json_data)
    response = requests.post(sheety_endpoint, json=json_data)
    print(response.text)
else:
    print("please enter correct email address")


import json

import requests
import datetime

APP_ID = "e2c4fded"
APP_KEY = "ea29dd216463e2cbe0dc5deecb492aa3"
GENDER = "female"
AGE = 26
WEIGHT_KG = 50
HEIGHT_CM = 168

today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")




parameters = {
 "query":input("Tell me which exercise you did: "),
 "gender":GENDER,
 "weight_kg":HEIGHT_CM,
 "height_cm":HEIGHT_CM,
 "age":AGE
}


headers = {
    "x-app-id": APP_ID,
    "x-app-key" : APP_KEY,
}
# parameters = {
#  "query":input("tyell me which exercise you did: ")
#  "gender":"female",
#  "weight_kg":72.5,
#  "height_cm":167.64,
#  "age":30
# }

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/ea7f56639807f76fd1f6362fcf1b6cbc/anithaWorkouts/workouts"

response = requests.post(nutritionix_endpoint, json=parameters, headers= headers)
result = response.json()

for exercise in result["exercises"]:
    calories = exercise["nf_calories"]
    duration = exercise["duration_min"]
    exercise = exercise["name"]

    sheety_json = {
        "workout" : {
            "date" : date,
            "time" : time,
            "exercise" : exercise.title(),
            "duration" : duration,
            "calories" : calories,
        }

    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheety_json,
                                   auth=("python", "jkhjhiklsdf424354aghgf" ))
    print(sheet_response.text)
#


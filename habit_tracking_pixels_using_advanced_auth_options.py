import requests
import datetime

date = datetime.datetime.now()
TODAY = date.strftime("%Y%m%d")
print(TODAY)

USERNAME = "practiceforpython"
TOKEN = "ehgh4oihj6pdh9yehhjk"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "momiji",

}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpont = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_parameters = {
    "date" : TODAY,
    "quantity" : input("How many kilometers did you cycle today? "),

}

# response = requests.post(pixel_endpont, json=pixel_parameters, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

update_pixel_endpoint_parameters = {
    "quantity" : "11.8"
}

response = requests.put(update_pixel_endpoint, json=update_pixel_endpoint_parameters, headers=headers)
print(response.text)

# response = requests.delete(update_pixel_endpoint ,headers=headers)
# print(response.text)
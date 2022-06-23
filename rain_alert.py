import requests
LAT = 40.433030
LON = -80.090660
api_key = "084918df477d8c75a9d9ad00ee600388"

parameters = {
              "lat":5.004870,
              "lon":-76.003120,
              "exclude":"current,minutely,daily",
              "appid":"084918df477d8c75a9d9ad00ee600388"}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
umbrella = False
for i in range(12):
    weather_data = response.json()["hourly"][i]["weather"][0]["id"]
    if int(weather_data) < 700:
        umbrella = True
if umbrella:
    print("Bring an umbrella")

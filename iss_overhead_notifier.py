import requests
import datetime
import smtplib
import time

MY_LAT = 40.440624
MY_LONG = -79.995888

my_email = "practiceforpython30@gmail.com"
my_password = "oaffoziqzxojnkfh"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True



def is_night():
    parameters = {"formatted":0}

    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()

    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])


    now = datetime.datetime.now().hour
    #print(now.hour)
    if now >= sunset or now < sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs= my_email,
                msg="Subject: Look Up\n\nThe ISS is above you in the sky"
            )

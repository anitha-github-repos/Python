import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "practiceforpython30@gmail.com"
my_password = "oaffoziqzxojnkfh"

URL = "https://www.amazon.com/Instant-Pot-Programmable-Pressure-Steamer/dp/B01B1VC13K/ref=dp_fod_3?pd_rd_i=B01B1VC13K&psc=1"

header = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=header)
HTML = response.text

soup = BeautifulSoup(HTML, features="lxml")

price_tag = soup.find("span", class_="a-offscreen")

price = price_tag.get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title_tag = soup.find("span", id="productTitle")
product_title = title_tag.get_text()
print(product_title.strip())


if price_as_float <= 100.0:
    message = f"{product_title.encode('utf-8').strip()} is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr="noreply@pricedrop.com",
            to_addrs=my_email,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{URL}"
            #msg=f"Subject: Amazon Price Alert!\n\n{product_title.strip()} is now {price}\n{URL}"
        )



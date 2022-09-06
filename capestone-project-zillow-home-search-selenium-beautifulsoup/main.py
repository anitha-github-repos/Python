import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import lxml

google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdGSVaR0UjdWY2-khE42-5vzYhwojuhXLlcfyBuFRnGTSYZBA/viewform?usp=sf_link"
#zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69125507932882%2C%22north%22%3A37.85923241333961%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69125507932883%2C%22north%22%3A37.859232413339626%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%5D%7D"


header = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

chrome_driver_path = "C:/Users/Vissu/desktop/chromedriver_win32/chromedriver.exe"

response = requests.get(url=zillow_url, headers=header)
time.sleep(5)
zillow_home_page = response.text

soup = BeautifulSoup(zillow_home_page, "html.parser")

price = soup.select("div div.list-card-price")
link = soup.select("div a.list-card-link")
address = soup.select("div a.list-card-link address")

property_price = []
property_link = []
property_address = []

for p in price:
    text_p = p.text
    property_price.append(text_p)
for l in link:
    text_l = l.get("href")
    property_link.append(text_l)

for a in address:
    text_a = a.text
    property_address.append(text_a)

print(property_price)
print(property_address)
print(property_link)

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(google_form_url)
time.sleep(5)

address_input = driver.find_elements(By.CSS_SELECTOR, "div.Xb9hP input")
#price_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div")
#link_input = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")


# address_input.send_keys("1160 pennsbury")
# price_input.send_keys("$1335")
# link_input.send_keys("https://www.zillow.com")

#keys = ["1160 pennsbury", "$1335", "https://www.zillow.com" ]



for k in range(len(property_address)):
    time.sleep(5)
    j = 0
    keys = [property_address[k], property_price[k], property_link[k]]
    print(keys)
    for i in address_input:
        #time.sleep(2)
        i.send_keys(keys[j])
        j +=1
    submit_button = driver.find_element(By.CSS_SELECTOR, "div.lRwqcd span span")
    submit_button.click()
    time.sleep(5)
    driver.get(google_form_url)
    #another_response = driver.find_element(By.CSS_SELECTOR, "div.c2gzEf a")
    #another_response.click()

responses_url = "https://docs.google.com/forms/d/1aXIvzh_FqtsTCf06MIhxQpeQFpfkbUcN6CZMBgQrfrY/edit#responses"
time.sleep(3)
sheet_create_button = driver.find_element(By.CSS_SELECTOR, "div.jovfwb div.M9Bg4d")
sheet_create_button.click()



# print(link.get("href"))
# rent = price.text
# print(address.text)
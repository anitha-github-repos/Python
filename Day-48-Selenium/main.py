from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Vissu/desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Instant-Pot-Programmable-Pressure-Steamer/dp/B01B1VC13K/ref=dp_fod_3?pd_rd_i=B01B1VC13K&psc=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(f"${price.text}")
# sleep(4)

driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
links = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")
events = {}
for n in range(len(times)):
    events[n] = {
        "time" : times[n].text,
        "name" : links[n].text,
    }
print(events)

# print(times)
# print(events)


driver.close()
# driver.quit()


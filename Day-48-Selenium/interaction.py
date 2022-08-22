from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
chrome_driver_path = "C:/Users/Vissu/desktop/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

#CASE1
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # count.click()
# portal = driver.find_element(By.LINK_TEXT, "Wikinews")
# # portal.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

#CASE2
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("sample")
fname.send_keys(Keys.TAB)
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("signup")
lname.send_keys(Keys.TAB)
email = driver.find_element(By.NAME, "email")
email.send_keys("samplemail@xyz.com")
email.send_keys(Keys.TAB)
# sign_up = driver.find_element(By.TAG_NAME, "button")
sign_up = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.btn-lg")
sign_up.send_keys(Keys.ENTER)


#driver.close()

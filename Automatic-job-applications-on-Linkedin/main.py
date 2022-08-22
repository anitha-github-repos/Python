import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/Vissu/desktop/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/checkpoint/lg/login")
username = driver.find_element(By.ID, "username")
username.send_keys("practiceforpython30@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("PandhiPig@9")
sign_in = driver.find_element(By.CLASS_NAME, "btn__primary--large[type='submit']")
sign_in.send_keys(Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3222912102&f_AL=true&keywords=python%20developer&sortBy=R")
#driver.get("https://www.linkedin.com/jobs/view/3226471902/?eBP=JOB_SEARCH_ORGANIC&recommendedFlavor=ACTIVELY_HIRING_COMPANY&refId=x4YboboHKyH%2FKxfXrrdQ2Q%3D%3D&trackingId=HhAAsjt%2BSaZMLnWjE%2FBfkQ%3D%3D&trk=flagship3_search_srp_jobs")

#title = driver.find_element(By.CSS_SELECTOR, "div a.job-card-list__title").get_attribute("href")
# print(title.get_attribute("href"))

all_listings = driver.find_elements(By.CSS_SELECTOR, "div a.job-card-list__title")

for listing in all_listings:
    print("Called")
    listing.click()
    time.sleep(5)

    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR, "div .jobs-apply-button--top-card .artdeco-button__text")
        easy_apply.click()
        time.sleep(5)
        #mobile_number = driver.find_element(By.CSS_SELECTOR, "div .display-flex input.ember-text-field")
        mobile_number = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if mobile_number.text == "":
            mobile_number.send_keys("111111111")
        submit_button = driver.find_element(By.CSS_SELECTOR, "div .justify-flex-end .artdeco-button__text")
        if submit_button.text == "Next":
            close_button = driver.find_element(By.CSS_SELECTOR, "div button.artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CSS_SELECTOR, "div button.artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, ".artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue


time.sleep(5)
driver.close()



#print(easy_apply.text)






submit_button.click()

# next_button = driver.find_element(By.CSS_SELECTOR, "div .justify-flex-end span.artdeco-button__text")
# next_button.click()
#
# next_button = driver.find_element(By.CSS_SELECTOR, "div .justify-flex-end span.artdeco-button__text")
# next_button.click()



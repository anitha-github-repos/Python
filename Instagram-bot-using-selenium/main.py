import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import ElementClickInterceptedException

my_email = "anitharamya102@gmail.com"
my_password = "PandhiPig@9"
similar_account = "chefsteps"

chrome_driver_path = "C:/Users/Vissu/desktop/chromedriver_win32/chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(By.CSS_SELECTOR, "div label input")
        password = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        #time.sleep(5)
        #username = self.driver.find_element(By.NAME, "username")
        #password = self.driver.find_element(By.NAME, "password")
        username.send_keys(my_email)
        password.send_keys(my_password)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        #login.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}/")
        time.sleep(15)
        follow = self.driver.find_element(By.CSS_SELECTOR, "header section ul li a")
        #follow = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        #follow = self.driver.find_element(By.XPATH, "//*[@id='mount_0_0_g1']/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div/span")
        time.sleep(2)
        follow.click()
        time.sleep(10)
        modal = self.driver.find_element(By.CSS_SELECTOR, "div div._aano")
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follows(self):
        all_follows = self.driver.find_elements(By.CSS_SELECTOR, "div._aano button")
        print(all_follows)

        for f in all_follows:
            try:
                f.click()
                print("clicked")
                time.sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element(By.CSS_SELECTOR, "div button._a9_1").click()




insta = InstaFollower()

insta.login()
insta.find_followers()
insta.follows()




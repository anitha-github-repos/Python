from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "practiceforpython40@gmail.com"
TWITTER_PASSWORD = "Anitharamya@9"
chrome_driver_path = "C:/Users/Vissu/desktop/chromedriver_win32/chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, "div a span.start-text ")
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        print(self.down.text)
        print(self.up.text)

    def get_tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(60)
        # print(self.driver.title)
        # 
        # sign_up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/svg/g/path[3]")
        # sign_up.click()
        # time.sleep(10)
        # base_window = self.driver.window_handles[0]
        # gmail_window = self.driver.window_handles[1]
        # self.driver.switch_to(gmail_window)
        # email = self.driver.find_element(By.XPATH, "")
        # password = self.driver.find_element(By.XPATH, "")
        # email.send_keys(TWITTER_EMAIL)
        # password.send_keys(TWITTER_PASSWORD)
        # password.send_keys(Keys.ENTER)
        # self.driver.switch_to(base_window)
        #time.sleep(10)
        tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")

        message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet.send_keys(message)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_button.click()
        time.sleep(2)
        self.driver.close()
        


bot = InternetSpeedTwitterBot()
#bot.get_internet_speed()
bot.get_tweet_at_provider()





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys
os.environ['TWITTER_USERNAME'] = 'IsaacC44739098'
os.environ['TWITTER_PASSWORD'] = 'Minnie1057'

PROMISED_DOWN = 1000
PROMISED_UP = 20
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_USERNAME = os.environ.get('TWITTER_USERNAME')
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class TwitterBot:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(2)
        on = True

        while on:
            try:
                self.download_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
                self.upload_speed = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
                on = False
            except:
                try:
                    notification_x_button = self.driver.find_element(By.CLASS_NAME, "notification-dismiss")
                    notification_x_button.click()
                    print("it works")

                except:
                    print("this got hit")
                    time.sleep(2)
        print(self.download_speed)
        print(self.upload_speed)
        return self.download_speed, self.upload_speed

        input("press something to quit: ")
        self.driver.quit()


    def tweet_at_provider(self):
        self.get_internet_speed()
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        username_input = self.driver.find_element(By.CSS_SELECTOR, ".css-901oao input")
        username_input.send_keys(TWITTER_USERNAME)
        username_input.send_keys(Keys.ENTER)
        time.sleep(3)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(4)
        tweet_box = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        tweet_box.send_keys(f"@comcast @Xfinity promises {PROMISED_DOWN}Mbps down/ {PROMISED_UP}Mbps up and I am receiving {self.download_speed}Mbps down/{self.upload_speed}Mbps up")
        time.sleep(3)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        post_button.click()
        time.sleep(10)
        self.driver.quit()


bot = TwitterBot(CHROME_DRIVER_PATH)
bot.tweet_at_provider()
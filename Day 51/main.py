from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"
CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 20)

        self.up = 0
        self.down = 0

    # -------------------------
    # 1. Speed test
    # -------------------------
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        try:
            go_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
            )
            go_button.click()

            # ⚠ better than fixed sleep (basic wait fallback)
            time.sleep(50)

            self.down = self.driver.find_element(
                By.XPATH,
                '//*[@id="container"]/div/div[3]//span'
            ).text

            self.up = self.driver.find_element(
                By.XPATH,
                '//*[@id="container"]/div/div[3]//div[3]//span'
            ).text

        except Exception as e:
            print("Speed test failed:", e)

    # -------------------------
    # 2. Twitter login + tweet
    # -------------------------
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        try:
            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            email_input.send_keys(TWITTER_EMAIL)
            email_input.send_keys(Keys.ENTER)

            time.sleep(3)

            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)

            time.sleep(5)

            tweet = (
                f"Hey Internet Provider, why is my internet speed "
                f"{self.down}down/{self.up}up when I pay for "
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
            )

            tweet_box = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tweet text']"))
            )
            tweet_box.send_keys(tweet)

            tweet_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetButtonInline']"))
            )
            tweet_button.click()

            time.sleep(2)

        except Exception as e:
            print("Tweet failed:", e)

        finally:
            self.driver.quit()


# -------------------------
# Run bot
# -------------------------
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time
import random

INSTAGRAM_USERNAME = os.environ['INSTAGRAM_USERNAME']
INSTAGRAM_PASSWORD = os.environ['INSTAGRAM_PASSWORD']

class InstaFollower:

    def __init__(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        # cookie popup
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='선택 가능 쿠키 거부']")
                )
            )
            cookie_button.click()
        except TimeoutException:
            pass

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        # username
        username_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        username_input.click()
        time.sleep(0.5)
        username_input.send_keys(INSTAGRAM_USERNAME)
        time.sleep(random.uniform(0.5, 1.0))

        # password
        password_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        password_input.click()
        time.sleep(0.5)
        password_input.send_keys(INSTAGRAM_PASSWORD)
        time.sleep(0.5)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/fifaworldcup/")
        time.sleep(3)

        followers_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "팔로워"))
        )
        followers_button.click()
        time.sleep(3)

    def follow(self):
        scroll_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//div[@style='overflow: hidden auto;'] | //div[@role='dialog']//div[contains(@class, '_xy39')]")
            )
        )
        last_height = 0
        clicked_users = set()

        while True:

            # follow buttons
            follow_buttons = self.driver.find_elements(
                By.XPATH,
                "//button[.//div[text()='팔로우']]"
            )

            for button in follow_buttons:
                try:
                    user = button.text

                    if user and user not in clicked_users:
                        self.driver.execute_script("arguments[0].click();", button)
                        clicked_users.add(user)

                        print(f"Followed: {user}")

                        time.sleep(random.uniform(2.5, 4.0))

                except:
                    continue

            # scroll down
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                scroll_box
            )

            time.sleep(random.uniform(2.0, 3.5))

            # check scroll end
            new_height = self.driver.execute_script(
                "return arguments[0].scrollHeight",
                scroll_box
            )

            if new_height == last_height:
                time.sleep(2)
                if new_height == self.driver.execute_script("return arguments[0].scrollHeight", scroll_box):
                    print("all accounts are followed.")
                    break

            last_height = new_height

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = InstaFollower()
    error_occurred = False

    try:
        bot.login()
        bot.find_followers()
        bot.follow()

    except Exception as e:
        error_occurred = True
        print(f"Error: {e}")

    finally:
            if not error_occurred:
                bot.quit()
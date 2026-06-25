from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
import time
import random

GOOGLE_EMAIL = "_email"
GOOGLE_PASSWORD = "_password"

# ----------------------------
# Driver setup
# ----------------------------
service = Service()
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20)

driver.get("https://tinder.com")


# ----------------------------
# helper functions
# ----------------------------
def random_sleep(a=1.0, b=2.0):
    time.sleep(random.uniform(a, b))


def safe_click(by, value, timeout=10):
    """Wait + click with retry handling"""
    for _ in range(3):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            return True
        except (StaleElementReferenceException, ElementClickInterceptedException):
            time.sleep(1)
    return False


def handle_popups():
    """Handle common Tinder popups"""
    try:
        # Match popup
        match = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
        match.click()
        return
    except NoSuchElementException:
        pass

    try:
        # Generic close buttons (cookie, etc.)
        close_btns = driver.find_elements(By.XPATH, "//button[contains(text(),'OK') or contains(text(),'Not Now') or contains(text(),'No Thanks')]")
        for btn in close_btns:
            try:
                btn.click()
                return
            except:
                pass
    except:
        pass


# ----------------------------
# Login flow
# ----------------------------
login_button_xpath = "YOUR_XPATH"
google_login_xpath = "YOUR_XPATH"

safe_click(By.XPATH, login_button_xpath)
safe_click(By.XPATH, google_login_xpath)

# window switch
base_window = driver.current_window_handle

try:
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    for handle in driver.window_handles:
        if handle != base_window:
            driver.switch_to.window(handle)
            break
except TimeoutException:
    print("Google login window did not open")
    driver.quit()
    exit()


# Google login (NOTE: may break depending on current Google UI)
try:
    email = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email.send_keys(GOOGLE_EMAIL)
    email.send_keys(Keys.ENTER)

    time.sleep(2)

    password = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password.send_keys(GOOGLE_PASSWORD)
    password.send_keys(Keys.ENTER)

except Exception as e:
    print("Google login failed:", e)


# switch back
driver.switch_to.window(base_window)


# ----------------------------
# Main loop
# ----------------------------
like_button_xpath = "YOUR_XPATH"

for i in range(100):
    try:
        handle_popups()

        like_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, like_button_xpath))
        )

        # fallback JS click (more stable)
        driver.execute_script("arguments[0].click();", like_btn)

        random_sleep(1.2, 2.8)

    except ElementClickInterceptedException:
        handle_popups()

    except StaleElementReferenceException:
        time.sleep(1)

    except TimeoutException:
        handle_popups()
        time.sleep(1)

    except Exception as e:
        print(f"Unexpected error at iteration {i}: {e}")
        time.sleep(1)
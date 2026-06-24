from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

ACCOUNT_EMAIL = os.environ.get("ID")
ACCOUNT_PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# try:
driver.get("https://www.linkedin.com/jobs/")

time.sleep(2)

# login
email_field = driver.find_element(By.ID, "session_key")
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(By.ID, "session_password")
password_field.send_keys(ACCOUNT_PASSWORD)

password_field.send_keys(Keys.ENTER)

time.sleep(2)
driver.refresh()
time.sleep(5)

# searching
job_input = driver.find_element(By.XPATH, '//input[@placeholder="Describe the job you want"]')
job_input.send_keys("Data Analyst Aachen")

job_input.send_keys(Keys.ENTER)

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "main"))
)

# edit location scale
location_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='button'][.//p[contains(text(),'km')]]")
    )
)

driver.execute_script("arguments[0].click();", location_button)

edit_button = driver.find_element(
    By.XPATH,
    "//button[.//span[contains(text(),'Within')]]"
)

driver.execute_script("arguments[0].click();", edit_button)

slider = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//input[@type="range"]')
    )
)

driver.execute_script("""
    arguments[0].value = '40';
    arguments[0].setAttribute('aria-label', 'Slider, 40');

    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
""", slider)

show_results_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(., 'Show results')]")
    )
)

driver.execute_script("arguments[0].click();", show_results_button)

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "main"))
)


# last 7 days
date_posted_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//div[@aria-label="Filter by Date posted"]/ancestor::div[@role="button"]')
    )
)

driver.execute_script("arguments[0].click();", date_posted_button)

past_week_radio = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//span[contains(text(),"Past week")]/ancestor::div[@role="radio"]')
    )
)
print("past_week_radio found")
driver.execute_script("arguments[0].click();", past_week_radio)
print("past_week_radio clicked")

past_week_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(., 'Show results')]")
    )
)
print("past_week_button found")
driver.execute_script("arguments[0].click();", past_week_button)
print("past_week_button clicked")

# finally:
    # driver.quit()


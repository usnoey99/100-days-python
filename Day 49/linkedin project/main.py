from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os

ACCOUNT_EMAIL = os.environ.get("ID")
ACCOUNT_PASSWORD = os.environ.get("PASSWORD")

if not ACCOUNT_EMAIL or not ACCOUNT_PASSWORD:
    raise RuntimeError("Environment variables ID / PASSWORD are not set.")

SEARCH_QUERY = "Data Analyst Aachen"
WAIT_TIMEOUT = 15

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, WAIT_TIMEOUT)


def safe_click(element):
    """JS click; also guards against the element going stale right before clicking."""
    driver.execute_script("arguments[0].click();", element)


try:
    driver.get("https://www.linkedin.com/jobs/")

    # ---------------- Login ----------------
    email_field = wait.until(
        EC.presence_of_element_located((By.ID, "session_key"))
    )
    email_field.send_keys(ACCOUNT_EMAIL)

    password_field = driver.find_element(By.ID, "session_password")
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)

    # Check for a security checkpoint (captcha/2FA) or login failure right after login
    time.sleep(2)
    if "checkpoint" in driver.current_url or "challenge" in driver.current_url:
        raise RuntimeError(
            "LinkedIn security checkpoint (captcha/2FA) detected. "
            "Please complete verification manually in the browser, then re-run the script."
        )

    # Force English UI (LinkedIn language redirect workaround)
    driver.refresh()

    job_input_locator = (By.XPATH, "//input[contains(@placeholder,'job')]")
    wait.until(EC.presence_of_element_located(job_input_locator))

    # ---------------- Search ----------------
    job_input = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[@placeholder="Describe the job you want"]')
        )
    )
    job_input.send_keys(SEARCH_QUERY)
    job_input.send_keys(Keys.ENTER)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))

    # ---------------- Set distance (km) ----------------
    location_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@role='button'][.//p[contains(text(),'km')]]")
        )
    )
    safe_click(location_button)

    edit_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[.//span[contains(text(),'Within')]]")
        )
    )
    safe_click(edit_button)

    slider = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="range"]'))
    )

    driver.execute_script(
        """
        arguments[0].focus();
        arguments[0].value = '40';
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
        """,
        slider,
    )

    show_results_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Show results')]"))
    )
    safe_click(show_results_button)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))

    # ---------------- Past week filter ----------------
    date_posted_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//div[@aria-label="Filter by Date posted"]/ancestor::div[@role="button"]',
            )
        )
    )
    safe_click(date_posted_button)

    past_week_radio = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//span[contains(., "Past week")]/ancestor::div[@role="radio"]')
        )
    )
    print("past_week_radio found")
    safe_click(past_week_radio)

    wait.until(lambda d: past_week_radio.get_attribute("aria-checked") == "true")
    print("past_week_radio clicked")

    past_week_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[.//span[contains(., 'Show results')]]")
        )
    )
    print("past_week_button found")
    safe_click(past_week_button)
    print("past_week_button clicked")

except TimeoutException as e:
    print(f"[Error] Timed out while waiting for an element: {e}")
    print("LinkedIn's UI may have changed, or the page is loading slowly. Check the browser state.")
except NoSuchElementException as e:
    print(f"[Error] Element not found: {e}")
except RuntimeError as e:
    print(f"[Aborted] {e}")
except Exception as e:
    print(f"[Unexpected error] {type(e).__name__}: {e}")

# Since detach=True, the browser stays open even if an error occurs.
# Uncomment the line below to close the browser once you're done debugging.
# driver.quit()
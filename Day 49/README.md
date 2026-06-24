## Day 49 - Automated Job Applications with Selenium

---

### 📌 Overview
Built a LinkedIn job search automation script using Selenium WebDriver.

The script searches for jobs based on a specified keyword, applies filters such as location radius and “Past week” posting date, and interacts with dynamic web UI elements.

Due to LinkedIn’s anti-bot protection mechanisms (e.g., checkpoint/captcha), full end-to-end automation may be interrupted during execution.

---

### 📝 Tasks

* Automated LinkedIn login using Selenium
* Searched for jobs based on a specified keyword
* Adjusted job search location radius dynamically
* Filtered job listings posted within the last 7 days
* Handled dynamic web elements and UI state changes
* Used JavaScript execution for reliable UI interactions
* Implemented explicit waits for stable automation flow

---

## 🧠 Notes

### Selenium Waits

Modern websites load content dynamically, so element availability cannot be assumed immediately.

Using `time.sleep()` is unreliable because load times vary.

Explicit waits ensure Selenium proceeds only when elements are ready for interaction.

Example:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "main"))
)
```

### JavaScript Click

Some web elements cannot be clicked normally because of overlays or custom UI behavior.

JavaScript can trigger the click directly.

Example:
```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

### Handling SVG / Dynamic UI Elements
Modern web applications often use nested or dynamically generated DOM structures, including SVG icons.

Instead of targeting icons directly, interactions should be performed on their parent or container elements.

Example:
```python
location_button = driver.find_element(
    By.XPATH,
    "//div[@role='button'][.//p[contains(text(),'km')]]"
)
```

### Filter Automation

Automated job filtering includes interacting with dynamic UI components such as sliders and dropdown filters.

Key actions:

- Adjusting location radius using a slider (React-based UI)
- Selecting “Past week” filter for job postings
- Applying filters via “Show results” button

Example:
```python
slider = driver.find_element(
    By.XPATH,
    "//input[@type='range']"
)

driver.execute_script("""
    arguments[0].focus();
    arguments[0].value = '40';
    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
    arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
    arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
""", slider)
```
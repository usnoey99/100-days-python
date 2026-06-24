## Day 49 - Automated Job Applications with Selenium

---

### 📌 Overview
Built a LinkedIn job automation bot using Selenium WebDriver.

The bot searches for jobs based on a specified role, filters listings posted within the last 7 days, saves all matching job postings, and follows the companies that posted them.

---

### 📝 Tasks

* Automated LinkedIn login using Selenium
* Searched for jobs based on a specified keyword
* Filtered job listings posted within the last 7 days
* Saved job postings for later review
* Followed companies associated with job listings
* Handled browser interactions and dynamic web elements
* Automated repetitive job search tasks

---

## 🧠 Notes

### Selenium Waits

Modern websites often load content dynamically.

Using `time.sleep()` is unreliable because the page may load slower or faster.

Explicit waits allow Selenium to continue only when an element is ready.

Example:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.ID, "button")
    )
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

### Handling SVG Elements

Icons are often created using SVG.

Instead of clicking the SVG directly, locate the clickable parent.

Example:
```python
location_button = driver.find_element(
    By.XPATH,
    "//svg[@id='location-marker-small']/ancestor::div[@role='button']"
)
```

### Filter Automation

Automated job filtering:

- Location radius adjustment
- Date posted filter selection
- Applying search conditions

Example:
```python
slider = driver.find_element(
    By.XPATH,
    "//input[@type='range']"
)

driver.execute_script(
    "arguments[0].value='40';",
    slider
)
```
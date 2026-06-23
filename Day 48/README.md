## Day 48 - Selenium Webdriver

---

### 📌 Overview

Learned how to automate web browsers using Selenium WebDriver.

Practiced locating web elements, interacting with web pages, and controlling browser actions.

Built a Cookie Clicker automation project using Selenium.

---

### 📝 Tasks

* Installed and configured Selenium WebDriver
* Controlled Chrome browser using Python
* Located web elements using different selectors
* Used Selenium to click buttons and input text
* Automated Cookie Clicker gameplay
* Collected cookie count and upgrade prices
* Implemented automatic purchasing logic based on available resources

---

## 🧠 Notes

### Selenium WebDriver

A tool that allows Python code to control a web browser.

Used for:

* Web automation
* Testing
* Repetitive browser tasks

Example:

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com")
```

### Finding Web Elements

Selenium provides different ways to locate HTML elements.

```python
from selenium.webdriver.common.by import By

element = driver.find_element(
    By.ID,
    "button"
)
```

Common selectors:

| Selector     | Example           |
| ------------ | ----------------- |
| ID           | `By.ID`           |
| Class Name   | `By.CLASS_NAME`   |
| Name         | `By.NAME`         |
| CSS Selector | `By.CSS_SELECTOR` |
| XPath        | `By.XPATH`        |
| Link Text    | `By.LINK_TEXT`    |

### find_element vs find_elements

`find_element()`:

* Returns a single element
* Throws an error if not found

```python
button = driver.find_element(
    By.ID,
    "submit"
)
```

`find_elements()`:

* Returns a list of elements

```python
links = driver.find_elements(
    By.TAG_NAME,
    "a"
)
```

### Interacting With Elements

Clicking:

```python
button.click()
```

Typing:

```python
search.send_keys("Python")
```

Keyboard actions:

```python
from selenium.webdriver.common.keys import Keys

search.send_keys(Keys.ENTER)
```

### Getting Attributes

Elements can contain useful information inside HTML attributes.

Example:

```python
item_id = element.get_attribute("id")
```

### Automating Tasks with Loops

Selenium can repeatedly perform actions by using loops.

Example:

```python
while True:
    cookie.click()
```

The bot continuously clicks the cookie and performs upgrade checks.

### Time Control

The `time` module can be used to control automation timing.

Example:

```python
timeout = time.time() + 5
```

The program checks conditions every few seconds instead of every loop.

### Dictionary Mapping

Dictionaries can connect upgrade prices with upgrade IDs.

Example:

```python
cookie_upgrades = {
    100: "cursor",
    500: "grandma"
}
```

This allows the program to select the most expensive affordable upgrade.

### WebDriver Wait

Sometimes elements are not ready immediately after loading.

Use explicit waits:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "button")
    )
)
```
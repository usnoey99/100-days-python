## Day 53 - Capstone Project: Data Entry Job Automation

---

### 📌 Overview
This capstone project applies everything learned over the past ~10 days of study.  

The goal of this project is to automate a real-world data entry workflow using Python.

The project combines **BeautifulSoup** for web scraping and **Selenium WebDriver** for browser automation. It extracts property data from a real estate website and automatically inputs the collected information into a Google Form.

This project demonstrates how web scraping and automation can be integrated to eliminate repetitive manual data entry tasks.


---

### 📝 Tasks
* Scrape property data from a real estate website
* Extract property addresses, prices, and listing links
* Clean and structure scraped data
* Open and interact with a Google Form automatically
* Fill in form fields with extracted data
* Submit multiple entries using browser automation
* Handle repetitive workflows efficiently

---

## 🧠 Notes

### Selenium 3 vs Selenium 4 (Latest Version)

Selenium has undergone a major structural update from version 3 to version 4.  
The main difference is not just syntax, but how the WebDriver is managed and how elements are located.

1) WebDriver Initialization

    **Selenium 3**

    Drivers had to be manually downloaded and the path had to be explicit provided.
    ```python
    driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
    ```
   
    **Selenium 4**

    Selenium Manager can automatically handle driver setup.
    ```python
    driver = webdriver.Chrom()
    ```
    Alternatively, a more explicit and modern approach:
    ```python
    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(service=Service())
    ```
   
2) Finding Elements

    **Selenium 3**

    Element-finding methods were directly attached to the driver.
    ```python
    driver.find_element_by_xpath("//div")
    driver.find_element_by_id("id")
    ```
   
    **Selenium 4**

    Uses the `By` class for clearer and more structured element selection.
    ```python
    from selenium.webdriver.common.by import By
    driver.find_element(By.XPATH, "//div")
    driver.find_element(By.ID, "id")
    ```
    
3) Waiting Strategy
    
    **Selenium 3**

    Mostly relied on static waits.
    ```python
    time.sleep(2)
    ```
   
    **Selenium 4**

    Encourages explicit waits for better stability.
    ```python
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div"))
    )
    ```
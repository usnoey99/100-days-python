## Day 52 - Instagram Follower Bot

---

### 📌 Overview
Built an automated Python bot using Selenium WebDriver that logs into Instagram, navigates to a target profile, opens the followers list, and automatically follows users from that list.

The bot demonstrates browser automation involving authentication, dynamic content loading, scrolling within modal windows, and repetitive user interactions.

Since Instagram's interface has changed significantly since the original course was published, the project was updated to work with the current website structure.

Due to Instagram's anti-bot protection, dynamic website structure, and frequent UI updates, the automation may require adjustments over time.

---

### 📝 Tasks
* Log in to Instagram automatically
* Navigate to a target profile
* Open the followers list
* Scroll through dynamically loaded followers
* Click the **Follow** button for each account
* Handle pop-ups and page loading
* Close browser safely after execution

---

## 🧠 Notes

### ## Day 52 - Instagram Follower Bot

---

### 📌 Overview
Built an automated Python bot using Selenium WebDriver that logs into Instagram, navigates to a target profile, opens the followers list, and automatically follows users from that list.

The bot demonstrates browser automation involving authentication, dynamic content loading, scrolling within modal windows, and repetitive user interactions.

Since Instagram's interface has changed significantly since the original course was published, the project was updated to work with the current website structure.

Due to Instagram's anti-bot protection, dynamic website structure, and frequent UI updates, the automation may require adjustments over time.

---

### 📝 Tasks
* Log in to Instagram automatically
* Navigate to a target profile
* Open the followers list
* Scroll through dynamically loaded followers
* Click the **Follow** button for each account
* Handle pop-ups and page loading
* Close browser safely after execution

---

## 🧠 Notes

### Selenium WebDriver Setup
This project uses Selenium WebDriver with ChromeOptions for browser automation.
```python
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
```
This approach ensures better compatibility with modern ChromeDriver versions and avoids deprecated configuration methods.

### Human-like Interaction Simulation
To reduce detection risk and improve stability, small random delays were added between actions.
```python
time.sleep(random.uniform(2.5, 4.0))
```
This helps simulate more natural user behavior during automation.
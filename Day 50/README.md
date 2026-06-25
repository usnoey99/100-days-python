## Day 50 - Auto Tinder Bot

---

### 📌 Overview
Built an automated Tinder bot using Selenium WebDriver.

The bot automates the login process, handles common pop-up dialogs, and performs repetitive swipe actions by interacting with Tinder's web interface.

Due to Tinder's anti-bot measures, account verification, and rate limits, automation may be interrupted during execution.

---

### 📝 Tasks
* Set up Selenium WebDriver and Chrome browser automation
* Navigate to Tinder website
* Implement login flow using Google authentication
* Handle multiple browser windows during OAuth login
* Detect and close common pop-ups (match alerts, notifications, cookies)
* Automate "Like" button clicks in a loop
* Add random delays to simulate human behavior
* Handle common Selenium exceptions (stale elements, click interception, timeouts)

---

## 🧠 Notes

### Handling Multiple Windows (OAuth Login)

```python
for handle in driver.window_handles:
    driver.switch_to.window(handle)
```
When using Google login, a new popup window is opened.

Because Selenium only interacts with the currently active window, so we must switch context before accessing login fields.

### Exception Handling in Selenium
Common issues:
- ElementClickInterceptedException → another element blocks click
- StaleElementReferenceException → element changed after page update
- TimeoutException → element did not load in time

Solution:

Use try/except blocks to ensure the script continues running even if errors occur.

### JavaScript Click (More Reliable Click)
```python
driver.execute_script("arguments[0].click();", element)
```
Some modern web apps (React-based like Tinder) block normal `.click()` actions.

JavaScript click bypasses some UI restrictions and is more stable.
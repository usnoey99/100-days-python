## Day 51 - Complaining Twitter Bot

---

### 📌 Overview
Built an automated Python bot using Selenium WebDriver that measures internet speed using Speedtest.net and automatically posts a complaint tweet to the internet service provider if the measured speed is below the promised threshold.

The bot demonstrates full end-to-end web automation, including performance testing, authentication handling, and social media interaction.

Due to dynamic website structures, anti-bot protection, and frequent UI changes on both Speedtest and Twitter (X), the automation may require adjustments over time.

---

### 📝 Tasks
* Measure internet speed using Speedtest
* Log in to Twitter automatically
* Generate and post a complaint tweet
* Handle page loading and pop-ups
* Close browser safely after execution

---

## 🧠 Notes

### Object-Oriented Automation
This project is structured using a class-based design to keep browser automation organized and reusable.

Methods are split into:
- Internet speed measurement
- Twitter login and posting

This improves readability and makes the bot easier to maintain.


### Selenium WebDriver Setup (Modern Approach)

```python
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
```
This is the recommended way to initialize Selenium in recent versions.

It replaces the older `executable_path` method and provides better compatibility with current ChromeDriver setups.


### Explicit Wait vs Fixed Sleep
```python
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))
)
```
Explicit waits are used instead of relying only on `time.sleep()`.

- Pages load dynamically
- Elements may not be immediately available
- Improves stability and reduces random failures
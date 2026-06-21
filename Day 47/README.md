## Day 47 - Amazon Price Tracker Project

---

### 📌 Overview

Built an Amazon price tracker that monitors a product page and automatically sends an email notification when the price drops below a target value.

Used web scraping with BeautifulSoup to extract product information and price data, then automated email alerts using SMTP.

---

### 📝 Tasks

* Send HTTP requests with custom headers
* Scrape product titles and prices from Amazon
* Parse and process scraped data
* Compare the current price with a target price
* Send automated email notifications
* Store sensitive credentials using environment variables

---

## 🧠 Notes

### HTTP Headers

HTTP headers provide additional information about a request or response.

When scraping websites, headers can be used to make requests appear more like those from a real web browser.

Example:

```python
headers = {
    "User-Agent": "...",
    "Accept-Language": "en-US,en;q=0.9"
}
```

### User-Agent

A User-Agent identifies the client making a request.

Many websites use it to determine whether the request comes from a browser or a bot.

Example:

```python
headers = {
    "User-Agent": "Mozilla/5.0 ..."
}
```

### python-dotenv

The `python-dotenv` package loads environment variables from a `.env` file.

Example:

```python
from dotenv import load_dotenv

load_dotenv()
```

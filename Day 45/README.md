## Day 45 - Scraping the Web with BeautifulSoup

---

### 📌 Overview
Learning how to scrape data from websites using BeautifulSoup.

Parsing HTML, selecting specific elements, and extracting information from both local HTML files and live websites. Building a project that scrapes a list of "100 Movies You Must Watch" from a web page.

---

### 📝 Tasks
- Learn the basics of web scraping
- Parse HTML using BeautifulSoup
- Find and select HTML elements
- Extract text and attributes from web pages
- Scrape data from a live website
- Build a movie list scraper project


---

## 🧠 Notes

### Web Scraping
Web scraping is the process of automatically extracting data from websites.

It involves sending requests to web pages, retrieving HTML content, and parsing that content to collect specific information.

Web scraping is commonly used for data collection, research, price monitoring, and data analysis.

### BeautifulSoup
BeautifulSoup is a Python library used for parsing HTML and XML documents.

It allows developers to navigate, search, and extract data from web pages, making it a popular tool for web scraping.

Example:
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
title = soup.title.string
```

### Parsing HTML
Parsing is the process of converting raw HTML into a structured format that can be searched and manipulated.

Example:
```
soup = BeautifulSoup(contents, "html.parser")
```

### prettify()
The `prettify()` method formats HTML into a readable, properly indented structure.

It is useful for inspecting and debugging HTML documents.

Example:
```
print(soup.prettify())
```

### find()

The `find()` method returns the first matching HTML element.

Example:
```
heading = soup.find(name="h1")
```

### find_all()

The `find_all()` method returns a list of all matching HTML elements.

Example:
```
links = soup.find_all(name="a", href=True)
```

### getText()

The `getText()` method extracts the text content from an HTML element.

Example:
```
text = tag.getText()
```

### get()
The get() method retrieves the value of an HTML attribute.

Example:
```
url = tag.get("href")
```

### HTML Attributes
Attributes provide additional information about HTML elements.

Example:
```
<a href="https://example.com">Visit</a>
```
In this example, href is an attribute.

### Scraping a Live Website
Live website scraping involves sending an HTTP request to a webpage and extracting data from the returned HTML.

Example:
```
import requests

response = requests.get(url)
html = response.text
```
Headers may be required to avoid blocking.

### ### select() and CSS Selectors
The `select()` method allows selecting elements using CSS selectors.

Example:
```python
soup.select(".titleline a")
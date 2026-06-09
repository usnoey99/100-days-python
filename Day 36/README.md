## Day 36 - Stock News Monitoring Project

---

### 📌 Overview
Today we built a stock price monitoring system that automatically checks for significant price changes in a company’s stock. If the stock price increases or decreases by more than a set threshold, the program fetches the latest related news articles using an API and sends them via SMS. This project combines multiple APIs to create an automated notification system that keeps users updated on important market movements.

---

### 📝 Tasks
- Fetch daily stock price data using the Alpha Vantage API
- Compare yesterday’s and the day before yesterday’s closing prices
- Calculate the percentage change in stock price
- Trigger the program when the price change exceeds a defined threshold (e.g., 1%)
- Fetch related news articles using the News API
- Format and send the top news headlines via Twilio SMS

---

## 🧠 Notes

### Stock Price API (Alpha Vantage)
The Alpha Vantage API provides real-time and historical stock market data.
- We use the TIME_SERIES_DAILY endpoint to get daily stock prices.
- Each response contains a dictionary of dates and price data.
- We compare the latest two closing prices to calculate price movement.

Example:
```python
yesterday_close = data_list[0]["4. close"]
day_before_close = data_list[1]["4. close"]
```
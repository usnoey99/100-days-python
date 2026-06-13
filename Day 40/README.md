## Day 40 - Capstone Part 2: The Flight Club

---

### 📌 Overview
Upgraded the Flight Deal Finder from Part 1 into a more complete flight notification service.

The application reads destination data and target prices from a Google Sheet, searches for available flights using the Amadeus API, identifies the cheapest flight for each destination, and sends notifications when a flight is cheaper than the predefined target price.

This project demonstrates how multiple APIs can work together to build an automated flight monitoring system. Google Sheets are used as a simple database, Amadeus provides flight data, and Twilio delivers notifications to users.

---

## 🧠 Notes

### Amadeus API Authentication
Before accessing flight data, the application must obtain an access token.

The Amadeus API uses OAuth authentication.

Example:
```python
body = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET
}
```
A successful request returns:
```python
{
    "access_token": "...",
    "expires_in": 1799
}
```
The token is then included in future requests using Bearer Authentication.

Example:
```python
headers = {
    "Authorization": f"Bearer {token}"
}
```

### Data Calculations with `datetime`
The application automatically searches for flights within a future date range.

Example:
```python
tomorrow = datetime.now() + timedelta(days=1)
```
Six months from today:
```python
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
```
These dates are passed to the flight search API.
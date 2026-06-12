## Day 39 - Capstone Part 1: Cheap Flight Finder

---

### 📌 Overview
Built the first part of a flight deal tracking application using multiple APIs. The goal is to monitor flight prices automatically and notify users when a flight becomes cheaper than a predefined target price.

Destination cities and target prices are stored in a Google Sheet. The program retrieves this data, searches for flight information, compares the current price with the target price, and sends a notification if a cheaper deal is found.

Originally designed to use the Amadeus Flight Search API. Since the Amadeus Self-Service APIs have been discontinued, mock flight data or alternative flight APIs can be used to complete the project.

---

### 📝 Tasks
- Read destination data from Google Sheets using the Sheety API
- Store and organize flight information using custom classes
- Search for flight prices using a flight search API
- Compare current flight prices against target prices
- Send notifications when a flight price falls below the target price
- Structure the project using multiple modules and classes

---

## 🧠 Notes

### Project Structure

The project follows an object-oriented design by separating responsibilities into different classes.

#### `DataManager`
Responsible for interacting with the Google Sheet through the Sheety API.

Responsibilities:
- Retrieve destination data from the spreadsheet
- Update spreadsheet records when needed
- Store city names, IATA codes, and target prices

Example data:

| City | IATA Code | Lowest Price |
|--------|--------|--------|
| Paris | PAR | 200 |
| Berlin | BER | 150 |
| Tokyo | TYO | 700 |

#### `FlightSearch`
Responsible for communicating with the flight search API.

Responsibilities:
- Search flights for a destination
- Retrieve current flight prices
- Find airport IATA codes from city names
- Return flight information to the main program

Typical workflow:

```python
flight_search = FlightSearch()
flight_data = flight_search.search_flight("PAR")
```
'FlightData'

Responsible for structuring and storing flight information.

Instead of passing around large JSON responses, important values are extracted and stored in a dedicated object.

Example:
```python
class FlightData:
    def __init__(self, price, origin, destination):
        self.price = price
        self.origin = origin
        self.destination = destination
```
- Cleaner code
- Easier access to flight information
- Better separation of concerns

`NotificationManager`

Responsible for sending notifications.

Originally implemented using Twilio.

- Send SMS alerts
- Send WhatsApp messages
- Format flight deal information

Example notification:
```
Low Price Alert!

Paris (PAR)
Price: £185

Departure: 2026-07-10
Return: 2026-07-20
```

### Separation of Responsibilities

Instead of putting everything inside `main.py`, each class focuses on a single task.

| Class               | Responsibility               |
| ------------------- | ---------------------------- |
| DataManager         | Google Sheets data           |
| FlightSearch        | Flight API requests          |
| FlightData          | Flight information structure |
| NotificationManager | SMS / WhatsApp notifications |
| main.py             | Coordinates all classes      |

This approach makes the project easier to maintain test, and extend.
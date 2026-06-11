## Day 38 - Exercise Tracking with Python and Google Sheets

---

### 📌 Overview
Building an exercise tracking application using Python and Google Sheets.

Using a nutrition and exercise API to interpret workout descriptions written in natural language, estimate calories burned, and store the results in a Google Sheet. Learned how to work with authenticated APIs and automate data logging.

---

### 📝 Tasks
- Use the Nutritionix Exercise API to process natural language workout descriptions
- Retrieve exercise details such as duration and calories burned
- Send workout data to a Google Sheet using the Sheety API
- Authenticate API requests using HTTP headers
- Store API credentials securely using environment variables
- Automate workout logging without manually entering spreadsheet data

---

## 🧠 Notes

### Nutritionix Exercise API
The Nutritionix Exercise API can analyze exercise descriptions written in natural language.

Example:
```python
exercise_data = {
    "query": "ran for 30 minutes"
}
response = requests.post(url, json=exercise_data, headers=headers)
result = response.json()
```
The API returns information such as:
- Exercise name 
- Duration 
- Calories burned

### Sheety API
The Sheety API allows Google Sheets to be used like a REST API.

This makes it possible to:

- Create spreadsheet rows with POST requests
- Update rows with PUT requests
- Delete rows with DELETE requests

Example:
```python
sheet_data = {
    "workout": {
        "date": "11/06/2026",
        "exercise": "Running",
        "duration": 30,
        "calories": 320
    }
}
response = requests.post(sheet_endpoint, json=sheet_data)
```

### Environment Variables
Environment variables allow sensitive information to be stored outside the source code.

Instead of hardcoding API keys:

API_KEY = "my_secret_key"

Store them as environment variables and access them using the `os` module:
```python
import os
API_KEY = os.getenv("API_KEY")
```
- Prevents exposing secrets in source code
- Safer when uploading projects to GitHub
- Makes it easier to use different credentials across environments

### The os Module
The os module provides access to operating system functionality.
Common use in API projects:
```python
import os
api_key = os.getenv("API_KEY")
```
- os.getenv() → Read environment variables
- os.environ[] → Access environment variables directly
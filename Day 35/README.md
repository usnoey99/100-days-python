## Day 35 - API Keys, Authentication, Environment Variables and Sending SMS

---

### 📌 Overview
Today we explored advanced API usage. We authenticated with an API key and fetched weather data from OpenWeatherMap, checking whether it will rain within the next 12 hours. We also learned how to send notifications using the Twilio API via SMS, and optionally through WhatsApp. Finally, we automated our Python script on PythonAnywhere, keeping our API keys and sensitive information hidden using environment variables.

---

### 📝 Tasks
- Fetch weather data from OpenWeatherMap API
- Check if rain is expected in the next 12 hours
- Send an SMS or WhatsApp message if rain is forecasted
- Hide API keys and credentials using environment variables
- Automate the script daily on PythonAnywhere

---

## 🧠 Notes

### API Key
An API key is a unique identifier provided by the API service.
- It allows the API provider to track how the service is being used.
- It can be used to grant access, enforce usage limits, or block requests if limits are exceeded.
- Each API may require a slightly different way to authenticate users, but most use some from of API key.

Example:
```python
api_key = "YOUR_API_KEY"
params = {"key": api_key}
response = requests.get("https://api.example.com/data", params=params)
```

### Twilio SMS Integration
1.Twilio Setup

  1. Create a Twilio account at [https://www.twilio.com](https://www.twilio.com).
  2. Obtain your **Account SID** and **Auth Token** from the dashboard.
  3. Get a Twilio phone number (from which messages will be sent).
  4. (Free account) Verify the phone numbers you want to send messages to.

2. Install Twilio Python SDK
```bash
pip install twilio
```


3. Basic Usage
```python
from twilio.rest import Client

# Replace with your own credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
twilio_number = "+1234567890"  # Twilio number
my_number = "+4910123456789"    # Verified recipient number

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Bring an umbrella ☂️ It will rain today!",
    from_=twilio_number,
    to=my_number
)

print(message.status)
```

4. Sending via WhatsApp
```python
message = client.messages.create(
    body="Bring an umbrella ☂️ It will rain today!",
    from_="whatsapp:+14155238886",  # Twilio Sandbox number
    to="whatsapp:+4910123456789"    # Verified WhatsApp number
)
```

### Environment Variables (Hiding API Keys)
Never hardcode API keys or sensitive credentials in our scripts. Use environment variables instead.
```bash
# Bash example
export OWM_API_KEY="your_openweathermap_api_key"
export TWILIO_SID="your_twilio_sid"
export TWILIO_TOKEN="your_twilio_auth_token"
export TWILIO_NUMBER="+1234567890"
export MY_NUMBER="+4910123456789"
```
Access them in Python:
```python
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
twilio_number = os.environ.get("TWILIO_NUMBER")
my_number = os.environ.get("MY_NUMBER")
```

### Automating the Script on PythonAnywhere
1. Log in to PythonAnywhere -> Tasks -> Add a new scheduled task
2. Set the command:
```bash
/usr/bin/python3.11 /home/yourusername/weather_check.py
```
3. Set the time
  We can remove the `while True` loop; PythonAnywhere will handle the scheduling
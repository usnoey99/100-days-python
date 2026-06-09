import requests
from datetime import datetime
import time
from twilio.rest import Client

# ==== OpenWeatherMap Setup ====
api_key = "YOUR_API_KEY"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_param = {
    "lat": 50.775345,
    "lon": 6.083887,
    "units": "metric",
    "appid": api_key
}

# https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# Weather Condition Codes: https://openweathermap.org/api/weather-conditions#693bf46d97d58c810416ef86


# ==== Twilio Setup ====
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
twilio_number = "+12345678901" # Twilio phone number (sender)
my_number = "+10987654321" # Verified recipient number (test number)

client = Client(account_sid, auth_token)

def send_sms(message):
    # Send SMS using Twilio API
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=my_number
    )



def check_weather():
    response = requests.get(OWM_Endpoint, params=weather_param)
    response.raise_for_status()  # Raise error for bad HTTP status codes
    weather_data = response.json()

    # Get forcast for the next 12 hours (3-hour intervals x4)
    weather_slice = weather_data["list"][:4]
    will_rain = False

    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]

        # Weather condition codes < 700 indicate rain/snow/thunderstorm
        if condition_code < 700:
            will_rain = True
            break

    if will_rain:
        message = "Bring an umbrella ☔ Rain is expected in the next 12 hours."
    else:
        message = "No rain expected in the next 12 hours."

    print(message)  # Print result to console
    send_sms(message)  # Send SMS notification



# ==== Scheduler (7 AM check) ====
while True:
    now = datetime.now()

    if now.hour == 7 and now.minute == 0:
        check_weather()
        time.sleep(60)  # prevent duplicate runs

    time.sleep(30)

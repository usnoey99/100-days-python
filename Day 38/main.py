import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_TOKEN = os.getenv("SHEET_TOKEN")


WEIGHT = 80
HEIGHT = 180
AGE = 30

base_endpoint = "https://app.100daysofpython.dev"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

exercise_endpoint = f"{base_endpoint}/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/4012d21386a53649ab632ded0ac7472a/myWorkouts/시트1"

exercise_text = input("Tell me which exercises you did:\n")

exercise_data = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=exercise_data, headers=headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_data = {
        "시트1": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_data, headers=sheet_headers)

    print(sheet_response.text)
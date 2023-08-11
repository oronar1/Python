#The example of running you can find on 
#https://replit.com/@MichaelBochkovs/workout-trackers#main.py

import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
APP_ID = os.environ.get("APP_ID")
APP_ID = os.environ.get("APP_ID","Message")
API_KEY = os.environ["API_KEY"]
API_KEY = os.environ.get("API_KEY") 
API_KEY = os.environ.get("API_KEY","Message")


BEARER_AUTH = os.environ["BEARER_AUTH"]
BEARER_AUTH = os.environ.get("BEARER_AUTH") 
BEARER_AUTH = os.environ.get("BEARER_AUTH","Message")


GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "175"
AGE = "36"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpont = "https://api.sheety.co/e2737edafdb922b01373644078033400/mbWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": BEARER_AUTH
    }

    sheet_response = requests.post(
        sheet_endpont,
        json=sheet_inputs,
        headers=bearer_headers
    )


    print(sheet_response.text)

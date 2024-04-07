import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 180
AGE = 24

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]
AUTHORISATION = os.environ["AUTHOR"]

date_now = datetime.now()
date = date_now.strftime("%d/%m/%Y")
time = date_now.strftime("%H:%M:%S")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": AUTHORISATION
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
data = response.json()
count = 0
for item in data["exercises"]:
    if isinstance(item, dict):
        exercise_name = data["exercises"][count]["name"]
        exercise_duration = data["exercises"][count]["duration_min"]
        exercise_calories = data["exercises"][count]["nf_calories"]
        count += 1
    new_parameters = {
        "workout":
            {
                "date": f"{date}",
                "time": f"{time}",
                "exercise": f"{exercise_name}",
                "duration": f"{exercise_duration}",
                "calories": f"{exercise_calories}"
            }

    }
    new_exercise = requests.post("https://api.sheety.co/59e7a521b0c05bab53c154dfe8ad79b9/workoutTracking/workouts",
                                 json=new_parameters, headers=headers)
    new_exercise_data = new_exercise.json()
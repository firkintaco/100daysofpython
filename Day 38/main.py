API_KEY = ""
appId = ""
import requests
from datetime import datetime
def add_row(exercise: str, duration: str, calories: str):
    """Add's row to Google Sheets using Sheetly"""
    header_params = {
        "Authorization": "Bearer workouttoken",
        "Content-Type": "application/json",
    }
    row = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    endpoint = "https://api.sheety.co/3550973c1df5dd761ce83da1ac8754b8/myWorkouts/workouts"
    response = requests.post(url=endpoint, json=row, headers=header_params)
    response.raise_for_status()
    if response.status_code == 200:
        print("Added row to sheet")

def ask_user():
    """Ask's user what he did today and generates values using Natural Language Processing"""
    header_params = {
        "x-app-key": API_KEY, # API KEY for authentication
        "x-app-id": appId # Nutritionix appId
    }

    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    request_body = {
        "query": input("What you did today?"),
        "gender": "male",
        "weight_kg": 80,
        "height_cm": 180,
        "age": "22"
    }
    response = requests.post(url=exercise_endpoint, headers=header_params, json=request_body)
    data = response.json()["exercises"]
    # For every exercise put data to google sheets
    for treeni in data:
        exercise = treeni["name"].title() # Exercise name
        duration = treeni["duration_min"] # Duration
        calories = treeni["nf_calories"] # Burned calories
        add_row(exercise, duration, calories)



ask_user()
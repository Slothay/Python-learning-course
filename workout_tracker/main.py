import requests
import os
from datetime import datetime

# Set up API Information to connect to Sheety
SHEETY_ENDPOINT = os.environ['SHEET_ENDPOINT']
TOKEN = os.environ['TOKEN']
sheety_headers = {
    'Content-Type': 'application/json',
    'Authorization': TOKEN
}

# Set up API Information to connect to Nutritionix API.
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
# Use API for natural language for exercise
ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
# Prompt user for what exercise they have done and save as parameter
exercise_done = input("Which exercise you did? ")
parameters = {
    'query': exercise_done
}
# Get the response from the API endpoint
response = requests.post(url=ENDPOINT, json=parameters, headers=headers)
exercises = response.json()
# make new dict for Sheety to work with the data
today = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%X'),

for training in exercises["exercises"]:
    sheet_input = {
        "workout": {
        'date': today,
        'exercise': training['name'].title(),
        'duration': training['duration_min'],
        'calories': training['nf_calories']
        }
    }
    # Make request to the Sheety API
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_input, headers=sheety_headers)
    #sheety_response.raise_for_status()

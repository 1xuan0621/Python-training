# 2022/03/07
import requests
from datetime import datetime

GENDER = 'male'
WEIGHT = '65'
HEIGHT = '164'
AGE = '22'
APP_ID = '105999b0'
API_KEY = 'd4b1310dba1844a78d583c9819e580a3'

excercise_text = input('Tell me which exercises you did: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

parameters = {
    'query': excercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE,
}

response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise', json=parameters, headers=headers)
result = response.json()
# print(result['exercises'][0]['user_input'])

day_now = datetime.now()

data = {
    'workout': {
        'date': day_now.strftime('%d/%m/%Y'),
        'time': day_now.strftime('%X'),
        'exercise': result['exercises'][0]['name'].title(),
        'duration': result['exercises'][0]['duration_min'],
        'calories': result['exercises'][0]['nf_calories'],
    }
}

sheet_headers = {
    'Authorization': 'Bearer hiiamyixuan'
}
sheet_endpoint = 'https://api.sheety.co/50d9778089ea9c04d99aac29d37cbf8a/myWorkouts/workouts'
sheet_response = requests.post(url=sheet_endpoint, json=data, headers=sheet_headers)
print(sheet_response.json())
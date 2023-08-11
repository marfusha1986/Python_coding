import requests
from datetime import datetime
import os

APP_ID ='f75fa47e'
API_KEY = '863464a0fe012d9241a7e6a72f9163b9	—'
USERNAME = 'marfusha marfusha'
PASS = 'pr7Duct!'
GENDER = 'FEMALE'
WEIGHT_KG = '68'
HEIGHT_CM = '163'
AGE = '37'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = 'https://docs.google.com/spreadsheets/d/1-GzEVOc2JNY7AkeD3V38Qrf5OnPXPeVuwUrDve4gh4o/edit#gid=0'

headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
}

exercise_text = input('Tell which exercise you did today?:')

parameters = {
    'query':exercise_text,
    'gender':GENDER,
    'weight_kg':WEIGHT_KG,
    'height_cm':HEIGHT_CM,
    'age':AGE,
}


response = requests.post(url=exercise_endpoint,json=parameters,headers=headers)
response.raise_for_status()
result = response.json()
print(result)

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')

for exercise in result['exercises']:
    sheet_inputs = {
        'workout':{
            'date':today_date,
            'time':now_time,
            'exercise':exercise['name'].uppercase(),
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheet_endpoint,json=sheet_inputs,auth=(f'{USERNAME}',f'{PASS}'))
    sheet_result = sheet_response.raise_for_status()


    print(sheet_result)

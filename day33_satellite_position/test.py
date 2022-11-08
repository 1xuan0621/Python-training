import requests
import datetime
MY_LAT = 23
MY_LONG = 120
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# iss_position = (longitude, latitude)
# print(data)
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,

}

response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]



time_now = datetime.datetime.now()

print(sunrise,'\n', sunset,'\n', time_now.hour)
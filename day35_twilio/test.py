import requests
from twilio.rest import Client

MY_API_KEY = '36b33bd40571dc77bcf07013a762f2ea'
MY_LAT = 25
MY_LONG = 121
account_sid = 'AC0458b97cd21ffecc79446b73d2f304ca'
auth_token = 'c8aed3cb5a8c483f598aafccb4083fa9'

weather_paremetes = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': MY_API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=weather_paremetes)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data['hourly']
weather_list = [n['weather'][0]['id'] for n in hourly_data[:12]]
# for n in hourly_data[:13]:
#     weather_list.append(n['weather'][0]['id'])
    # if n['weather'][0]['id'] < 800:
    #     print('bring umbralla')
    #     break
for i in weather_list:
    if int(i) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going tp rain today. Remember to bring an umbralla ",
            from_='+14345054642',
            to='+886983839151'
        )
        print(message.status)
        break 
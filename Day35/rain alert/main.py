import requests
from twilio.rest import Client


account_sid = "AC96ff8f1e4119a93e0b9f1473ba29abe4"
auth_token = "16b02064e9abf5f13b15db6c38a22b80"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
parameters = {
    'lat':41.037071,
    'lon':28.885160,
    'appid':api_key,

}


response = requests.get(OWN_Endpoint,params= parameters)
response.raise_for_status()
data=response.json()
weather_slice = data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='It is going to rain today.Remember to bring an umbrella.',
        from_='+12187182869',
        to="+905366458227"
    )


    print(message.status)


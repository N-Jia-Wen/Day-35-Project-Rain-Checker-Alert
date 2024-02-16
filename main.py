import requests
from twilio.rest import Client

MY_LAT = 1.352083
MY_LONG = 103.819839
OPENWEATHER_API_KEY = "Type your OpenWeatherMap account's API Key here"
OPENWEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

twilio_acc_sid = "Type your twilio account sid here"
twilio_auth_token = "Type your twilio authentification token here"
twilio_phone_no = "Type the virtual phone number generated via twilio here"
verified_phone_no = "Type your personal phone number that is verified on your twilio account here"
bring_umbrella = False

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OPENWEATHER_API_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get(url=OPENWEATHER_API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

for number in range(len(weather_data)):
    three_hour_data = weather_data[number]
    time_utc = three_hour_data["dt_txt"]

    # Main weather condition is the 1st item of list with key "weather"
    weather_id = three_hour_data["weather"][0]["id"]
    if weather_id < 700:
        bring_umbrella = True

if bring_umbrella is True:
    client = Client(twilio_acc_sid, twilio_auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Make sure to bring an umbrella ☂️.",
            from_=twilio_phone_no,
            to=verified_phone_no
        )

    print(message.status)

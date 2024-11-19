import requests as requests
from twilio.rest import Client

theApi = "https://api.openweathermap.org/data/2.5/onecall"
key = "0ee75066456cb47815337ad20ead0778"
theDict = {
    "lat": 48.86544875702591,
    "lon": 2.526501332939488,
    "exclude": "current,alerts,minutely,daily",
    "appid": key,
}

responses = requests.get(theApi, params=theDict)
data = responses.json()
hourly = data["hourly"][:12]

willRain = False


for i in range(len(hourly)):
    if hourly[i]["weather"][0]["id"] < 700:
        willRain = True

if willRain:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "ACbb17af5807818a3bbc5a71d0b92445ff"
    auth_token = "a71ef286037a5d64fa2c4210b5c7fd79"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring an umbrella, it is gonna rain",
        from_='+16065590885',
        to='+33635719503'
    )
    print(message.status)



import requests as requests
from datetime import datetime

Api_id = "30dc7342"
Api_key = "9f1a33b8a07c51b381660f9c39dddd58"

header_param = {
    "Content-Type": "application/json",
    "x-app-id": Api_id,
    "x-app-key": Api_key,
}
track_endPoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("tell me witch exercises you did ?")

response = requests.post(url=track_endPoint, headers=header_param, json={"query": f"{query}"})
resultsTraining = response.json()
exercisesList = resultsTraining["exercises"]
print(exercisesList)

sheetyGoogle_endPoint = "https://api.sheety.co/fb350e200ce6c77a5d8b293aefa37c05/workoutTrackingRefresh/workouts"

todayDay = datetime.now().strftime("%d/%m/%Y")
todayHour = datetime.now().strftime("%H:%M:%S")


for i in exercisesList:
    sheety_params = {
        "date": todayDay,
        "time": todayHour,
        "exercise": (i["name"]).title(),
        "duration": int(float(i["duration_min"])),
        "calories": int(i["nf_calories"]),
    }

    track_param = {
        "workout": sheety_params,
    }

    header = {
        "Authorization": "Basic YmlsbGdhdGU6VEhST1VHSGhlbGw4MThALzhf",
    }
    print(track_param)

    refreshSheet = requests.post(url=sheetyGoogle_endPoint, json=track_param, headers=header)

    print(refreshSheet.text)
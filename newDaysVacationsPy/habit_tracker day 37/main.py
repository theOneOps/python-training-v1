import requests

#creation of the account on Pixela

pixela_Endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": "adbjpi93se27D2dXp",
    "username": "billgate",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

request = requests.post(url=pixela_Endpoint, json=user_param)
print(request.text)


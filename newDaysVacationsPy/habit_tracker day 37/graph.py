import requests

# creation of the account on Pixela

graph_Api = "https://pixe.la/v1/users"
userName = "billgate"
token = "adbjpi93se27D2dXp"

graph_Endpoint = f"{graph_Api}/{userName}/graphs"

graph_param = {
    "id": "graph1",
    "name": "Calory Spend",
    "unit": "Kcal",
    "type": "float",
    "color": "momiji",
}

graph_param_header = {
    "X-USER-TOKEN": token,
}

request = requests.post(headers=graph_param_header, url=graph_Endpoint, json=graph_param)
print(request.text)

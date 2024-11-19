import requests


graph_Api = "https://pixe.la/v1/users"
userName = "billgate"
token = "adbjpi93se27D2dXp"

id = "graph1"

pixelToAdd_endpoint = f"{graph_Api}/{userName}/graphs/{id}"

graph_param_header = {
    "X-USER-TOKEN": token,
}

pixel_param = {
    "date": "20220725",
    "quantity": "2.2",
}

request = requests.post(json=pixel_param, url=pixelToAdd_endpoint, headers=graph_param_header)
print(request.text)
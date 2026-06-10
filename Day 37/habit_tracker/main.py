import requests
from datetime import datetime

USERNAME = "usnoey"
USERTOKEN = "poiuytrewq123456789"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USERTOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "Unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": USERTOKEN
}
graph_response = requests.post(graph_endpoint, json=graph_params, headers=headers)
print(graph_response.text)


# Post new data
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date": today,
    "quantity": "12.2"
}
pixel_response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)

# Update the data
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
new_pixel_data = {
    "quantity": "50.9"
}
new_pixel_response = requests.put(update_endpoint, json=new_pixel_data, headers=headers)
print(new_pixel_response.text)

# Delete the data
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
delete_pixel_data = {
    "date": today
}
delete_pixel_response = requests.delete(delete_endpoint, json=delete_pixel_data, headers=headers)
print(delete_pixel_response.text)

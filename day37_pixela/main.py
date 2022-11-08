# 2022/03/07
import requests
from datetime import datetime
pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = 'hiiamyixuan'
USER_NAME = 'yixuan'

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    "notMinor": "yes",
}

# pixela_response = requests.post(url=pixela_endpoint, json=user_params)
# print(pixela_response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Programing Graph',
    'unit': 'Hour',
    'type': 'float',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# graph_response = requests.post(url=graph_endpoint ,json=graph_config , headers=headers)
# print(graph_response.text)

post_pixel_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/graph1'

today = datetime.now()

post_pixel_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '2',
}
# print(today.strftime("%Y%m%d"))
# post_pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(post_pixel_response)

update_endpoint = f'{pixela_endpoint}/yixuan/graphs/graph1/20220307'

update_data = {
    'quantity': '3',
}

# update_response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(update_response.text)

delete_endpoint = update_endpoint = f'{pixela_endpoint}/yixuan/graphs/graph1/20220307'
delete_response = requests.delete(url=delete_endpoint, headers=headers)
print(delete_response.text)
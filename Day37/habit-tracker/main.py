import requests
from datetime import datetime

today = datetime.now()

USERNAME = 'marfusha'
TOKEN = 'hjgdjshgdsjhdgshdgj'
GRAPH_ID = 'graph1'
DATE = today.strftime('%Y%m%d')

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id':GRAPH_ID,
    'name':'Learning Coding Graph',
    'unit':'Hour',
    'type':'float',
    'color':'momiji',
}

headers = {
    'X-USER-TOKEN':TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

post_endpoint = f'{graph_endpoint}/{GRAPH_ID}'


post_config = {
    'date': DATE,
    'quantity':input('How much did you coding today?'),
}
# response = requests.post(url=post_endpoint,json=post_config,headers=headers)
# print(response.text)

update_post = f'{post_endpoint}/{DATE}'
update_data = {
    'quantity': '15.0'
}

# response = requests.put(url=update_post,json=update_data,headers=headers)
# print(response.text)

response = requests.delete(url=update_post,headers=headers)
print(response.text)



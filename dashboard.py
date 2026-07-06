import requests
from pprint import pprint

response=requests.get("https://jsonplaceholder.typicode.com/users")
data=response.json()
pprint(data)
first_user=data[0]
print(first_user)
print(type(first_user))
print(first_user["name"])
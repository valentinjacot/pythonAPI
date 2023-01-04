import requests

response = requests.get("https://fantasy.trashtalk.co/")
print(response.content)

#This works
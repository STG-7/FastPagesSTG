import requests

url = "http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5"

response = requests.request("GET", url)

print(response.text)
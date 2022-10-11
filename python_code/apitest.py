import requests, json


url = "https://us-zip-code-information.p.rapidapi.com/"

querystring = {"zipcode":"92127"}

headers = {
	"X-RapidAPI-Key": "6cef6d9f81mshf9a1793ed8d336ap1c4e09jsn658eb44a2a5f",
	"X-RapidAPI-Host": "us-zip-code-information.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
locations = json.loads(response.text)
lat = ""
lon = ""
for location in locations:
  lat =  location["Latitude"]
  lon = location["Longitude"]


  url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lon":lon,"lat":lat, "units": 'imperial'}

headers = {
	"X-RapidAPI-Key": "6cef6d9f81mshf9a1793ed8d336ap1c4e09jsn658eb44a2a5f",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

json_object = json.loads(response.text)

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)

for tempvalue in json_object.get("data"):
    print(tempvalue["app_temp"])
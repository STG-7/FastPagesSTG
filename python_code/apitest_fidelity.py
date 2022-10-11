import requests

url = "https://fidelity-investments.p.rapidapi.com/v2/auto-complete"

querystring = {"q":"Alphabet"}

headers = {
	"X-RapidAPI-Key": "6cef6d9f81mshf9a1793ed8d336ap1c4e09jsn658eb44a2a5f",
	"X-RapidAPI-Host": "fidelity-investments.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
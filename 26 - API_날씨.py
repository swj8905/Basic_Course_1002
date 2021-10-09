import requests # pip install requests
import json

api_key = "96760007b86e03e82a20e1c1f1b98c89"
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={api_key}")
result = json.loads(data.text) # json --> 딕셔너리
print(result["name"])
print(result["weather"][0]["main"])
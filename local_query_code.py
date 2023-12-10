import requests

url = "http://localhost:8000/generate"
data = {
        "prompt": "San Francisco is a",
        "temperature": 0,
        "top_p":1,
        "max_tokens":200
        }

response = requests.post(url, json=data)

print(response.text)


import requests

url = "http://localhost:8000/generate"
data = {
        "prompt": "The law of gravity was discovered by",
        "temperature": 0.8,
        "top_p":1,
        "max_tokens":200
        }

response = requests.post(url, json=data)

print(response.text)


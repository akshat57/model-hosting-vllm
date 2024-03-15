import requests

data = {
    'model': '/data/akshat/models/Llama-2-13b-chat-hf',
    'prompt': 'Wo liegt München in Deutschland?',
    'temperature': 0.2,
    'max_tokens': 200,
    'logprobs':2,
    }

response = requests.post('http://0.0.0.0:8000/v1/completions', json=data)
print(response.json())

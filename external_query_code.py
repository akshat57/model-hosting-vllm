import requests

data = {
    'model_prompt': 'Wo liegt München in Deutschland?',
    'temperature': 0.2,
    'max_tokens': 200,
    'logprobs':3
    }

response = requests.post('http://crtx.eecs.berkeley.edu:8002/query_model', json=data)
print(response.json())

import requests

data = {
    'system_prompt': 'Example prompt',
    'user_prompt': 'Example text',
    'temperature': 0.2,
    'top_p': 0.95,
    'max_tokens': 200
    }

response = requests.post('http://lexi.eecs.berkeley.edu:8002/query_model', json=data)
print(response.json())

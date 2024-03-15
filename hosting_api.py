from flask import Flask, request, jsonify
from typing import Tuple
import requests

app = Flask(__name__)


def query_local_model(model_prompt, temperature, max_tokens, logprobs):
    #pre define url and model prompt
    url = "http://0.0.0.0:8000/v1/completions"
    #model_prompt = "<s>[INST] <<SYS>>\n{your_system_message}\n<</SYS>>\n\n{user_message_1} [/INST]"

    #model_prompt = model_prompt.replace('{your_system_message}', system_prompt).replace('{user_message_1}', user_prompt)

    data = {
        "model": '/data/akshat/models/Llama-2-13b-chat-hf',
        "prompt": model_prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
        'logprobs':logprobs,
        }


    response = requests.post(url, json=data)
    response = response.json()

    return response, model_prompt



@app.route('/query_model', methods=['POST'])
def get_response() -> Tuple[str, int]:
    # Parse the JSON data from the request
    data = request.json
    
    # Extract variables from the JSON data
    model_prompt = data.get('model_prompt', '')
    temperature = data.get('temperature', 0.0)
    max_tokens = data.get('max_tokens', 0)
    logprobs = data.get('logprobs', 0)

    #query local model
    response, model_prompt = query_local_model(model_prompt, temperature, max_tokens, logprobs)
    #response_text = response['text'][0]
    #response_text = response_text.replace(model_prompt, '').strip()

    # Return a JSON response
    return jsonify({
        'response':response
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
